# Round 2 Assessment — Submission Package

This repository contains both requested tasks in separate folders. Task 1 and Task 2 are related only through the optional software-lab/capstone proposal; their reports and evidence remain separate.

## Task 1 — Faculty Leave & Class-Coverage Management
Folder: [`task-1-faculty-leave/`](task-1-faculty-leave/)

Includes the current-state process report, dated evidence log, a browser prototype, the five required synthetic test scenarios, test results, a net-time-saving scenario including review/support effort, AI-use/contribution disclosure, limitations and screenshots of the simulated approval path. Open [`prototype/index.html`](task-1-faculty-leave/prototype/index.html) to run the demo.

## Task 2 — Curriculum Audit and Redesign
Folder: [`task-2-curriculum-audit/`](task-2-curriculum-audit/)

Includes a provisional 166-credit baseline and balanced 166-credit redesign scenario, 12 course decisions with rationale, three dated job-role comparisons, a five-exercise AI verification log, a capstone/lab proposal, source register, validation record, and the interactive course-and-credit explorer. Open [`app/index.html`](task-2-curriculum-audit/app/index.html) in a modern browser.

## Key evidence and limitations
- Task 1 current-process details were reported verbally by a faculty member and relayed by the student on 24 October 2026. The precise SL sequence, NEL/EL procedures, approval authority, replacement confirmation rules and actual time measurements remain unconfirmed. Timetable expansion, leave balances and cap values are synthetic.
- Task 1's illustrative time-saving scenario is **not measured college data**: it models 26 baseline staff-minutes versus 16 proposed staff-minutes, or 10 minutes/38.5% in the scenario, including review and support effort.
- Task 2's course list comes from portal screenshots for Semesters I–VII plus the student's reported 15-credit internship. The exact registered programme/batch syllabus and applicable regulations were not obtained. Proposed credit movements are conditional design scenarios, not approved changes.
- The demos are not production systems; they have no database, secure authentication, server-side authorization or live integrations. See the task-specific reports for full limitations.

## Validation summary
- Task 1: seven client-side rule assertions passed; the normal request → replacement acceptance → coordinator review → HOD approval → faculty notification flow was manually verified in the browser. Test results and scope limits are in `task-1-faculty-leave/tests/`.
- Task 2: `python task-2-curriculum-audit/evidence/verify_exercises.py` passed 12 scripted assertions (8 CS101 and 4 CS102 checks). The interactive explorer is self-contained; see `task-2-curriculum-audit/analysis/validation.md` for remaining manual checks and limits.

## Submission links
- **GitHub repository:** https://github.com/sanju-2005/round2-assignment
- **Named release URL:** https://github.com/sanju-2005/round2-assignment/releases/tag/round2-submission-v1
- **Full commit URL (released revision):** https://github.com/sanju-2005/round2-assignment/commit/53cd35aa63de86e7d9feb7884221bc3b94799d69

The commit URL above identifies the preserved revision attached to the named release. If this package is uploaded as a new commit, update this line with the new commit URL as well, while retaining the release URL.
