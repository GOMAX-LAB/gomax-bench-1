PRAGMA foreign_keys=ON;
CREATE TABLE dispatch(session_id TEXT PRIMARY KEY,service_date TEXT NOT NULL,start_time TEXT NOT NULL,end_time TEXT NOT NULL,service_type TEXT NOT NULL,provider TEXT NOT NULL,worker TEXT NOT NULL,volunteer TEXT,site TEXT NOT NULL,cohort TEXT NOT NULL);
CREATE TABLE attendee(session_id TEXT NOT NULL REFERENCES dispatch(session_id),intake TEXT NOT NULL,PRIMARY KEY(session_id,intake));
CREATE TABLE funding(session_id TEXT NOT NULL REFERENCES dispatch(session_id),fund TEXT NOT NULL,cost_kind TEXT NOT NULL,amount REAL NOT NULL CHECK(amount>=0),PRIMARY KEY(session_id,fund,cost_kind));
CREATE INDEX worker_calendar ON dispatch(worker,service_date,start_time);
