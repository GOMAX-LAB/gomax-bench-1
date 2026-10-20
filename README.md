# GOMAX BENCHMARK for AI Work You Can Act On

**An AI agent can reach the right final decision and still fail the job.**

In one GOMAX medical-device review, a leading LLM produced all eight required sections and correctly concluded that the submission was not ready to file. It scored 5%. The grading record found that its proposed next steps included testing demands whose applicability had not been established, while important evidence gaps remained unresolved. A cautious conclusion had not produced a usable review.

That is the problem GOMAX BENCHMARK is built to measure. **Can an agent turn real industry materials into work that another professional can verify and act on?**

In engineering, completing a report is only part of completing an assignment. A recommendation must survive a return to the source files. Its calculations must be reproducible. Its risk assessment must cover the right place and time. If the evidence is insufficient, the deliverable must explain what is blocked and what would resolve it.

As a China-based data and annotation partner working with foundation-model developers in China and the United States, we treat those requirements as part of the data we build. GOMAX applies that approach to evaluation: the unit of assessment is a professional assignment, including the evidence and deliverables needed to carry it through.

## Contents

- [What existing benchmarks leave unresolved](#what-existing-benchmarks-leave-unresolved)
- [Introducing GOMAX BENCHMARK](#introducing-gomax-benchmark)
- [Building the evaluation around real deliverables](#building-the-evaluation-around-real-deliverables)
- [What the first results show](#what-the-first-results-show)
- [Where completed work breaks down](#where-completed-work-breaks-down)
- [What this means for industrial AI](#what-this-means-for-industrial-ai)

## What existing benchmarks leave unresolved

Recent benchmarks have made substantial progress toward real work. GDPval evaluates occupational deliverables. AssetOpsBench tests industrial operations. EngiWorld examines professional engineering software. Terminal-Bench-Science evaluates scientific research workflows. Their published designs already include much more than question answering.

The remaining challenge for an industrial buyer is interpretation. A strong result on one of these evaluations does not, by itself, establish that an agent can review a particular commissioning dossier, reconcile a clinical delivery history, or identify the smallest justified correction to a registration package. These assignments depend on which evidence is admissible, how conflicting records are resolved, and whether the final recommendation remains consistent across deliverables.

| Benchmark | What its published design measures | The question GOMAX makes explicit |
| --- | --- | --- |
| GDPval | Expert comparison of economically valuable work across 44 occupations. Its initial evaluation is one-shot. | Can the deliverable preserve the evidence, version history, and decision boundaries required for a specific industrial handoff? |
| AssetOpsBench | Industrial asset operations and maintenance, including multi-step agent workflows in a simulated IoT environment. | Can the agent reconcile heterogeneous project records and produce a defensible review beyond an asset-operation workflow? |
| EngiWorld | Tasks across professional engineering applications, with verifiers for geometry, physical feasibility, and design-rule compliance. | Can the agent establish which records justify a decision to proceed and which unresolved contradictions block it? |
| Terminal-Bench-Science | Expert-curated scientific workflows in containerized environments, with programmatic verification of concrete outputs. | Can the agent make an evidence-grounded professional judgment when the work also requires applicability decisions, conflict resolution, and corrective action? |

These are differences in emphasis and intended use. GOMAX's contribution is to make the path from source evidence to an actionable industry decision a central object of evaluation.

## Introducing GOMAX BENCHMARK

GOMAX BENCHMARK contains assignments across five domains, using the benchmark's own taxonomy. Each assignment has a recipient who needs to do something with the result. A validation engineer must decide whether a new compressor can enter a production-connected trial. A clinical-data manager must determine what can be delivered, withdrawn, or held after source records and permissions change. A community-service manager must produce an executable schedule that remains consistent with funding and access constraints.

The files reflect those responsibilities. Inputs include inspection reports, drilling records, factory and site acceptance records, clinical case materials, spreadsheets, and spatial datasets. Outputs include Word reports, Excel workbooks, JSON event records, SQLite databases, GeoTIFF files, and reproduction scripts. The task determines which artifacts are required.

All of the cases originate in China, supported by top-tier expert rosters—including academician teams—for domain annotation and validation. For us, the advantage is access to the records and practitioners behind consequential work. This collection brings infrastructure, equipment commissioning, clinical operations, research, and public services into the same evaluation effort. It lets us preserve the real-world complications that make an assignment difficult: conflicting reports, outdated historical records, incomplete test evidence, and shifting scope.

That expertise matters at every decision point—knowing when a borehole rules out an anomaly, when a later report supersedes a warning, or when a proposed fix goes beyond what the evidence justifies. These granular, professional distinctions are the true substance of a useful evaluation.

## Building the evaluation around real deliverables

GOMAX separates task instruction, execution environment, and verification logic. Each task runs in a reproducible environment and returns a numerical reward, and verification can be programmatic or model-based, whichever fits the task.

Each task begins with a real industry assignment that specifies the professional role, the available evidence, the scope of the decision, and the deliverables required. We then prepare the underlying materials through de-identification, structuring, annotation, and evaluation design, taking care to preserve the relationships a professional would have to reconstruct to do the work.

The rubrics are what make that work testable. Rather than scoring a final answer in isolation, they decompose each task into criteria that separate the different layers of evidence and reasoning—raw observations, intermediate interpretations, prior expert judgments, and the agent's own review—and then check properties such as coverage, chronology, missing evidence, and consistency across every deliverable the task produces. Each criterion carries an explicit weight, and verification can be programmatic or model-based depending on what the criterion tests.

This level of annotation makes failure diagnosable. Instead of a single low score, a developer can see exactly what went wrong and where in the task it happened—a gap in coverage, a broken dependency between deliverables, or a conclusion drawn without the evidence to support it.

Saved reports retain per-criterion scores, weights, written judging rationales, and individual attempts, and they separate execution or grading exceptions from genuine zero scores—so a failed run is never silently counted as a valid zero.

## What the first results show

In the October 18 evaluation snapshot, gpt-6.1-sol leads with **67.68%**, followed by gpt-6-astra at **57.99%** and deepseek-flash at **54.40%**. The listed models were evaluated using the claude-code agent, with reasoning effort recorded as high.

| Rank | Model identifier | Score (%) |
| ---: | --- | ---: |
| 1 | gpt-6.1-sol | 67.68 |
| 2 | gpt-6-astra | 57.99 |
| 3 | deepseek-flash | 54.40 |
| 4 | kimi-k3 | 39.83 |
| 5 | claude-fable-5-1 | 36.67 |
| 6 | MiniMax-M3 | 19.32 |
| 7 | claude-opus-5-5 | 17.09 |

GPT-6.1 Sol leads the leaderboard with roughly 68%. GPT-6 Astra follows at approximately 58%, with DeepSeek Flash close behind at 54%.

Only three of the seven models score above 50%, while the remaining four fall below 40%.

### Performance across selected assignments

The tables below present results for selected assignments across the benchmark's domains. Scores are normalized and reported as percentages. Short model labels follow the order of the overall leaderboard. Bold values identify the highest score in each row.

#### Engineering sciences

| Assignment | 6.1 Sol | 6 Astra | DeepSeek | Kimi K3 | Fable 5.1 | MiniMax M3 | Opus 5.5 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Tunnel risk review | 58.3 | 47.6 | **70.0** | 43.5 | 55.0 | 40.3 | 39.5 |
| Airfoil research review | **81.1** | 57.4 | 38.1 | 37.3 | 20.3 | 16.2 | 23.5 |
| Airfoil retest handoff | **91.7** | 87.5 | 73.7 | 71.2 | 63.5 | 40.1 | 19.2 |
| Compressor commissioning | **87.0** | 71.0 | 62.0 | 51.0 | 50.0 | 28.0 | 25.0 |

#### Earth sciences

| Assignment | 6.1 Sol | 6 Astra | DeepSeek | Kimi K3 | Fable 5.1 | MiniMax M3 | Opus 5.5 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Geoscience field-course planning | **63.7** | 20.1 | 50.8 | 48.6 | 35.2 | 0.0 | 0.0 |

#### Life sciences

| Assignment | 6.1 Sol | 6 Astra | DeepSeek | Kimi K3 | Fable 5.1 | MiniMax M3 | Opus 5.5 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Microbial remediation | 67.0 | **70.0** | 69.0 | 35.0 | 37.0 | 33.0 | 32.0 |
| Thyroid clinical-data delivery | 48.5 | 50.3 | **76.3** | 39.6 | 45.0 | 11.2 | 10.7 |

#### Natural sciences

| Assignment | 6.1 Sol | 6 Astra | DeepSeek | Kimi K3 | Fable 5.1 | MiniMax M3 | Opus 5.5 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Hydrogenation process selection | **82.5** | 76.5 | 62.7 | 57.4 | 62.0 | 39.9 | 39.1 |

#### Social sciences

| Assignment | 6.1 Sol | 6 Astra | DeepSeek | Kimi K3 | Fable 5.1 | MiniMax M3 | Opus 5.5 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Medical-device registration | 33.0 | 14.0 | **38.0** | 5.0 | 11.5 | 5.0 | 6.0 |
| IVD reagent-kit registration | 10.0 | 9.0 | **12.0** | 3.0 | 0.0 | 0.0 | 1.0 |
| Community-service operations | 90.9 | **100.0** | 30.3 | 39.4 | 21.2 | 10.6 | 6.1 |
| Rongqiao service reorganization | **98.5** | 92.4 | 69.7 | 47.0 | 39.4 | 7.6 | 3.0 |

## Where completed work breaks down

### A tunnel review that changed the risk picture

**The assignment.** Reconcile 17 reports into a traceable geological-risk review for two tunnel working faces. The deliverables must preserve both the location of a risk and changes in its status over successive reporting periods.

**What happened.** Deepseek-flash earned 70% on this task, yet the saved grading record identifies failures with direct consequences for the review. For the interval DK279+348 to DK279+479.4, the rubric requires a continuous red-warning phase. The output instead represented relevant events as yellow and left the interval DK279+378 to DK279+423.6 without a corresponding event for the same risk.

The model also failed to preserve a second red-warning phase associated with unstable surrounding rock. The grading record says it used the absence of water-inrush facts to limit that phase to yellow, although the relevant mechanism involved falling blocks, sliding, collapse, and roof failure. Evidence about water did not resolve the separate structural hazard.

**Why it matters.** A reviewer needs the right mechanism attached to the right interval and reporting period. If an output suppresses a warning or leaves part of the interval uncovered, the next person cannot reconstruct the risk picture reliably from the delivered files.

This problem was not confined to one model. In gpt-6-astra's second attempt, scored at 48.5%, two events covered DK293+307.6 to DK293+299.6 and DK293+289.6 to DK293+286.6. A 10-meter interval remained between them. The judge credited aspects of its evidence handling but rejected the incomplete coverage.

**What usable work requires.** Check that event intervals jointly cover the required area, keep distinct hazard mechanisms separate, and explain each change from an earlier risk state to a later one. Consistency within the written narrative is insufficient if part of the physical interval disappears.

### A correct decision with an unusable correction plan

**The assignment.** Review the registration materials for an automated seminal-plasma biochemical analyzer and determine whether the package can be submitted. The task contains 52 effective attachments and requires a review against the specified regulatory reference date.

**What happened.** MiniMax-M3 produced the required eight substantive sections and identified the product correctly. It also concluded that the package could not be submitted directly. Its recorded score was 5%.

The grading record explains the disconnect. The report demanded third-party registration testing unconditionally and extended its proposed work to biocompatibility studies without first establishing applicability. Its action list placed additional documentation and studies ahead of resolving the product, environment, software, and network baseline. The agent had produced a list of things to do, but the list did not respect the dependencies needed to close the review.

There was a subtler failure in the eight-year service-life claim. The agent noticed conflicting temperature, humidity, and altitude conditions and proposed harmonizing the parameters. It did not establish that the life-evaluation evidence covered the final environmental limits. Making the documents agree would still leave the underlying claim unsupported.

**Why it matters.** An industrial team needs to know what is wrong, what evidence already exists, and what additional work is justified. A blanket refusal coupled with excessive or misordered corrective work can delay a project without resolving its actual uncertainty.

**What usable work requires.** Establish the product configuration and the applicability of each requirement, reconcile the existing evidence against that configuration, and specify the remaining justified corrections in dependency order. The quality of a review lies in that reasoning as well as in its final decision.

## What this means for industrial AI

The two cases expose a common problem. An agent can produce substantial work while losing a relationship that determines whether the work is usable: a hazard and its location, a warning and its date, a service-life claim and the conditions under which it was tested.

For model developers, those failures suggest concrete targets for improvement. Training examples should preserve the links between claims and evidence, including rejected interpretations and unresolved conditions. Evaluations should reward complete spatial and temporal coverage and corrective actions that follow from the actual gap. A fluent explanation should not compensate for a contradiction in the delivered artifact.

For industry teams, GOMAX offers a way to investigate readiness at the level of an assignment. Before handing a workflow to an agent, inspect whether it can preserve the facts and constraints that the next professional depends on. The relevant evidence may be a reproducible calculation, a recoverable delivery state, or a justified decision to withhold approval.

For a data and annotation company, this changes what high-quality data must contain. A valuable example includes the source record, its applicability, the reasoning boundary, the resulting artifact, and the reason a plausible alternative fails. That gives model developers a specific behavior to improve and industry practitioners a specific behavior to verify.

Our aim is to connect industry practice to model improvement and bring the improvement back into the same workflows. Real assignments expose failures; expert annotation makes those failures precise; evaluation makes progress visible. GOMAX BENCHMARK measures whether that progress produces work another professional can responsibly use.
