"""服务站派单离线导入工具 2.1"""
import argparse,csv,sqlite3,json
from pathlib import Path
def main():
 p=argparse.ArgumentParser();p.add_argument('--csv-dir',required=True);p.add_argument('--database',required=True);a=p.parse_args()
 target=Path(a.database)
 if target.exists():raise SystemExit('目标库已存在，请选择新的派单库文件名')
 con=sqlite3.connect(target)
 try:
  con.executescript(Path(__file__).with_name('dispatch_schema.sql').read_text(encoding='utf-8'))
  con.execute('BEGIN')
  for tab in ['dispatch','attendee','funding']:
   with (Path(a.csv_dir)/(tab+'.csv')).open(encoding='utf-8-sig',newline='') as f:
    r=csv.DictReader(f);cols=[x[1] for x in con.execute('PRAGMA table_info('+tab+')')]
    if r.fieldnames!=cols:raise ValueError(tab+'字段不符: '+str(cols))
    con.executemany('INSERT INTO '+tab+' VALUES ('+','.join('?' for x in cols)+')',[[row[c] or None for c in cols] for row in r])
  bad=con.execute("SELECT session_id FROM dispatch WHERE end_time<=start_time OR service_type NOT IN ('到户','小组')").fetchall()
  if bad:raise ValueError('时间或类型不合要求: '+str(bad[:5]))
  if con.execute('PRAGMA foreign_key_check').fetchall():raise ValueError('关联记录缺失')
  con.commit()
  print(json.dumps({t:con.execute('SELECT count(*) FROM '+t).fetchone()[0] for t in ['dispatch','attendee','funding']},ensure_ascii=False))
 except Exception:
  con.rollback();raise
 finally:con.close()
if __name__=='__main__':main()
