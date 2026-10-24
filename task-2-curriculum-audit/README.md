# Task 2 — Curriculum Audit and Redesign

## Status and scope

This is a provisional student audit built from portal screenshots for Semesters I–VII and the student's report that the Semester VIII internship carries 15 credits. The baseline has **51 rows and 166 credits**. Three proposed modules bring the comparison explorer to **54 rows**. A balanced scenario keeps the total at 166.

The exact registered programme name, admission-batch syllabus, curriculum version and regulations have not been obtained. The public IFHE pages list CSE (Artificial Intelligence), CSE (AI & Data Science), and CSE (AI & Machine Learning) separately; the accessible public structure does not fully match the course codes/semester arrangement in the screenshots. Do not treat this draft as an official syllabus or approved credit change. [Official public structure](https://www.ifheindia.org/icfai-tech-school-hyderabad/icfaitech-btech-program-structure) | [B.Tech CSE (Artificial Intelligence) programme page](https://www.ifheindia.org/icfaitech-school-hyderabad/icfaitech/ugprograms/btech-cse-artificial-intelligence)

## Contents

- `data/curriculum.csv` — provisional semester course data and source-status labels.
- `research/job_descriptions.md` — three real, dated role pages, skills, role-level caveats and curriculum implications.
- `research/sources.md` — source register with URLs and access dates.
- `analysis/course_audit.md` — findings and 12 course decisions grounded in course titles and job evidence.
- `analysis/proposed_curriculum.md` — proposed credit transfers, 24.7% scope calculation, prerequisites, approval conditions and fallback.
- `analysis/capstone_proposal.md` — faculty leave/class-cover workflow turned into a synthetic-data software lab/capstone.
- `analysis/ai_verification_log.md` — five AI-assisted exercises with prompts, model/date, output, method and limitations. Two Python exercises have local scripted results pasted by the student; the remaining source cross-checks used AI assistance and are identified honestly.
- `analysis/feedback_and_contribution.md` — actual contribution, AI use, missing feedback and limitations.
- `analysis/validation.md` — credit/code checks and browser-test boundary.
- `app/index.html` — self-contained interactive course search/filter and credit comparison tool.

## Open the interactive explorer

Open `app/index.html` in a modern browser; no packages, accounts or live college integration are required. Use the semester and category filters, search field and “Show proposed redesign credits” switch. Semester cards show whole-semester totals even while the course table is filtered.

## How to interpret the redesign

The scenario conditionally moves four credits from DS303, EC308, OE418 and OE801 into three proposed practical modules (1 + 1 + 2). This is a design hypothesis, not an assertion that those courses are unimportant or that their credits can legally be changed. The defined core scope counts eight existing courses marked UPDATE plus four courses proposed for conditional one-credit reductions: **41/166 = 24.7%**. Other courses mentioned in the audit are retain decisions and possible later assessment ideas, not part of that quantified scope. If regulations do not permit any credit movement, use the proposed activities inside existing course credits instead.

## Honest validation status

The student reported a local run of `verify_exercises.py` on Windows/Python 3.14 with all 12 scripted checks passing. The student also shared the explorer output showing the expected 166-credit baseline/proposed total and semester totals after a display bug was fixed. A full automated browser test suite, official admission-batch regulations and stakeholder feedback are not available. See the linked validation and limitations records.
