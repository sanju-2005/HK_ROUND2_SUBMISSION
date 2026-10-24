# Validation record

**Record date:** 23 October 2026. Distinguish checks run by the preparation environment from the local Windows console output pasted by the student.

| Check | Result/status | Evidence or remaining limitation |
|---|---|---|
| CSV course rows | 51 provisional baseline rows; 3 proposal rows; 54 total rows in explorer | Extracted from student screenshots for Semesters I–VII; internship row is student-reported. |
| Semester credit totals | 20, 24, 24, 24, 24, 19, 16, 15 | Sum = 166. Credits are provisional. |
| Balanced redesign | Four one-credit reductions and three additions of 1 + 1 + 2 credits | Current 166; proposed 166; net 0. Subject reductions remain conditional. |
| Redesign scope | 41 unique current course credits in the defined core redesign scope: eight UPDATE courses plus four conditional REDUCE candidates | 41 ÷ 166 × 100 = 24.70%. Count method disclosed in `proposed_curriculum.md`. |
| App JavaScript syntax | `node --check` passed for extracted inline JavaScript during preparation | No automated browser test suite was run. |
| Interactive browser display | Student shared the course-explorer output after the semester-total filter issue was corrected; output showed 54 rows, baseline/proposed totals of 166 and semester totals matching the provisional data | This is a limited smoke test, not full end-to-end verification for every filter combination. |
| CS101 local test run | Student pasted Windows PowerShell output: 8/8 checks passed | Environment reported as Python 3.14; 8 scripted assertions. |
| CS102 local test run | Same student-reported run: 4/4 checks passed; reproducible script included | Hashable examples and the tested unhashable-item exception only. |
| Five AI-assisted exercises | Five prompts, model/date, output, and verification/limitations recorded | Two exercises have student-shared local script results; three concept/source checks were AI-assisted. Do not misstate them as independently reviewed by the student. |
| Official admission-batch syllabus/regulations | Not obtained | Kept visible as a key limitation; proposal is not an official revision. |
| Faculty/graduate feedback | Not obtained | No feedback was invented; credit scenario remains unreviewed. |

## Manual checks recommended before release

1. Open `app/index.html` in Chrome/Edge and reset to All semesters/All categories.
2. Confirm baseline and proposed total are both 166.
3. Toggle proposed redesign and check DS303, EC308, OE418 and OE801 each reduce by one credit, while `NEW-S5`, `NEW-S6` and `NEW-S7` add 1, 1 and 2 credits.
4. Check each semester remains at 20, 24, 24, 24, 24, 19, 16 and 15 credits.
5. Test search for `Generative AI` and at least one category filter. Semester comparison cards intentionally remain whole-semester totals when the displayed table is filtered.
6. Keep the source limitation and lack of stakeholder approval in the README/report.


### Semester-card filter consistency

The explorer calculates semester cards from the full course dataset rather than the filtered table, so all eight semester totals remain visible and correct while searching or filtering. The filtered-credit summary and course rows respond to the active filters. This behavior was checked by inspecting the render logic; a full automated browser test suite was not run.
