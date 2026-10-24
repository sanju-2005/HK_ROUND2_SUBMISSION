# Task 1 — Faculty Leave & Class-Coverage Management

## Deliverables
- `report.md` — reported current process, workflow map, proposed workflow, roles/statuses/fallback, five required test scenarios, risks, time-saving scenario, AI-use and limitations.
- `evidence/evidence-log.csv` — dated source register; separates verbal report, synthetic data and assumptions.
- `prototype/index.html` — self-contained browser demo with Faculty, Department Coordinator and HOD views.
- `tests/test-cases.csv` and `tests/test-results.csv` — synthetic acceptance tests and recorded outcomes.
- `calculations/time-savings-scenario.csv` — net staff-time scenario including review and support effort.
- `evidence/screenshots/` — student-shared screenshots of simulated replacement acceptance and HOD approval notification.

## Run the demo
Open `prototype/index.html` in Chrome or Edge. No install or server is required. Keep the same tab open while switching accounts; refreshing clears the in-memory request.

### Demo accounts
- Faculty/Pavan: `pavan` / `pavan123`
- Other faculty examples: `ananya` / `ananya123`, `vikram` / `vikram123`, `sneha` / `sneha123`, `arjun` / `arjun123`, `neha` / `neha123`, `rahul` / `rahul123`
- Department Coordinator: `coordinator` / `coord123`
- HOD: `hod` / `hod123`

These are fictional demo credentials. They are not real staff accounts.

## What the demo shows
1. Faculty selects leave category/date/class and finds possible cover candidates.
2. Faculty records a proposed replacement, messages them and records a simulated accept/decline.
3. Department Coordinator checks the request and forwards it for HOD review.
4. HOD records approval or rejection; rejection requires a reason. The requesting faculty can view the decision and note.

## Data and limits
The faculty-reported process was relayed verbally by the student on 24 October 2026. CL was described as Google Form → print → sign → submit to clerk. The SL route was described as a form or email to the HOD followed by a form and clerk submission, but the exact sequence is not confirmed. NEL and EL procedures, official approval order, cover-confirmation rules, balance-check rules, and LoP policy remain unknown. The HOF portal is intentionally excluded. Section A is based partly on student-provided timetable information; other sections, additional staff assignments, leave balances and caps (CL 12, SL 10, NEL 10, EL 15 demo units) are synthetic.

The portal is a front-end simulation: no database, real messaging/notifications, secure authentication, server-side authorization, or official college approval. The time-saving figures and 5/10/20-requests-per-month sensitivity examples are illustrative assumptions, not measured results or actual college request volumes. Real policy and faculty availability must be confirmed before deployment.

## Current verification status
The seven on-page client-side rule assertions passed. The student manually completed the normal end-to-end demo on 24 October 2026: replacement recorded, message sent and accepted, coordinator forwarded the request, HOD approved, and the faculty status page displayed the final decision and note. The rejection branch is included in the test record; retest it in the final UI if time permits.
