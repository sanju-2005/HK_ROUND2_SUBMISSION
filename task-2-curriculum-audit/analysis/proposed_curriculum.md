# Proposed curriculum redesign and credit balance

## Design principles
1. Preserve the programme's broad CS, math, AI and domain foundations.
2. Upgrade outcomes and assessments inside existing technical courses before adding many new standalone courses.
3. Add a small amount of explicit practice in engineering habits that appear in dated AI job descriptions.
4. Keep the proposed total equal to the 166-credit provisional baseline.
5. Treat all credit movement as conditional until the official admission-batch scheme, compulsory/elective designations and approval rules are confirmed.

## Reallocation ledger (provisional proposal only)

| Semester | Existing course | Current credits | Proposed credits | Change | Proposed recipient/use |
|---|---|---:|---:|---:|---|
| V | DS303 Blockchain Technology | 3 | 2 | -1 | Software Testing, Git and API Basics (new 1-credit practical, Sem V) |
| VI | EC308 Embedded Systems | 3 | 2 | -1 | MLOps and Model Deployment (new 1-credit practical, Sem VI) |
| VII | OE418 Foundation for VR/AR Systems | 3 | 2 | -1 | Responsible GenAI Product Lab receives part of reallocated credits |
| VII | OE801 English Language for Competitive Exams | 3 | 2 | -1 | Responsible GenAI Product Lab receives part of reallocated credits |
| V | Software Testing, Git and API Basics (proposed) | 0 | 1 | +1 | New practical course; requires programming/OOP |
| VI | MLOps and Model Deployment (proposed) | 0 | 1 | +1 | New practical course; requires coding practice and introductory ML |
| VII | Responsible GenAI Product Lab (proposed) | 0 | 2 | +2 | New lab; requires NLP/GenAI and programming foundations |
| **Net** | **Credits reallocated** |  |  | **0** | **Total remains 166** |

### Semester-credit check
- Semester V: -1 from DS303 +1 new practical = 24 credits (unchanged).
- Semester VI: -1 from EC308 +1 MLOps = 19 credits (unchanged).
- Semester VII: -1 from OE418 -1 from OE801 +2 GenAI Lab = 16 credits (unchanged).
- Semesters I–IV and VIII are unchanged.
- Programme total after proposed transfer = **166 credits**, subject to the baseline itself being confirmed.

**Critical caveat:** this is an analytical design scenario, not an approved change. The labels “OE” do not by themselves prove a course is freely reducible/elective. Do not implement any reduction without verifying the exact regulations, required learning outcomes, accreditation/university rules, and programme-owner approval. If credits are fixed, keep course credit values and implement the same improvements as modules/labs inside existing credits instead.

## Material redesign scope calculation

The assignment asks for changes affecting roughly 20–25% of programme credits. To avoid double-counting, the proposed scope counts the current credit values of unique existing courses where outcomes/assessment are materially redesigned, including the four courses proposed for conditional 1-credit reductions. New courses receive released credits and are not counted again in this numerator.

| Affected existing course | Credits counted once |
|---|---:|
| CS101 Computer Programming — input validation and unit-test basics | 4 |
| CS102 Data Structures — tested implementations/complexity evidence | 4 |
| CS201 OOP Concepts — modular design, Git and tests | 4 |
| CS203 Design and Analysis of Algorithms — edge cases and complexity evidence | 3 |
| CS206 DBMS — robust SQL and data validation | 4 |
| DS202 Industry Coding Practice — API and engineering workflow | 3 |
| DS304 Machine Learning — reproducible model evaluation | 4 |
| DS305 Data Wrangling and Visualization — provenance/leakage-safe preparation | 3 |
| DS303 Blockchain Technology — credit/content review is conditional | 3 |
| EC308 Embedded Systems — credit/content review is conditional | 3 |
| OE418 VR/AR Systems — credit/content review is conditional | 3 |
| OE801 English for Competitive Exams — credit/content review is conditional | 3 |
| **Unique current credits affected** | **41** |

Calculation: 41 ÷ 166 × 100 = **24.70%** (about 24.7%), within the requested 20–25% range. The four new course credits are the balanced destinations of four reallocated credits; they are not added again to the affected-credit numerator. This counts the current credits of eight existing courses whose assessment/content is in the core implementation scope, plus the four courses proposed for conditional one-credit reductions. Courses discussed as possible future assessment improvements in the audit's KEEP rows (DS306, CS305, DS311, DS408, CS307, SP301 and Internship) are not part of this quantified scope. New courses receive released credits and are not added again to the numerator. Another scope definition could produce a different percentage, so this boundary is stated explicitly.

## Prerequisite and delivery map

- Computer Programming → Data Structures/OOP → Industry Coding Practice and Software Testing/Git/API Basics.
- Data Structures + Discrete Mathematics + math foundations → Algorithms and AI/ML courses.
- Data Wrangling/DBMS → Machine Learning → Deep Learning/NLP/Computer Vision/Generative AI.
- NLP/GenAI + Software Testing/API Basics → Responsible GenAI Product Lab.
- Machine Learning + Software Testing/Git/API Basics → MLOps and Model Deployment.
- Special Project → prototype, tests, model/system evaluation, README, limitations, and deployment/recovery demonstration.

These are logical proposed dependencies inferred from subject titles, not verified official prerequisites. Confirm prerequisites in the official syllabus before final submission.

## How to assess the proposed change

For each revised module, use a small rubric: problem framing (10%), implementation correctness (25%), test coverage/edge cases (15%), data/model evaluation quality (20%), reproducibility/version control (10%), safety/privacy/limitations (10%), and communication/documentation (10%). Adjust to faculty policy if this proposal were ever considered for implementation.

## Regulatory conditions and fallback

If the governing rules do not permit credit redistribution or course reduction, the fallback is a **content-and-assessment redesign within current credit allocations**: add the practical outcomes as labs, assignments or project rubrics without changing the transcript credits. This preserves the total and avoids asserting authority the student does not have.


## Task 1 workflow carried into a proposed lab/capstone

The accompanying [`capstone_proposal.md`](capstone_proposal.md) develops the faculty leave workflow into a small, synthetic-data software project. It defines statuses, roles, validation, exception recovery and the five required negative/normal cases. This is the required cross-link between the two tasks; Task 1 and Task 2 remain separate analyses.
