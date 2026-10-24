# Task 1 — Faculty Leave & Smart Class-Coverage Management System

**Status: working draft; faculty validation pending.** This is a process-improvement proposal and synthetic prototype, not an official college policy or deployed system.

## 1. Executive summary

The process selected for investigation is faculty leave management and arranging cover for affected classes. On 24 October 2026, the student reported information provided verbally by a faculty member. The reported process differs by leave category: Casual Leave (CL) is requested through a Google Form, then printed, signed and submitted to the clerk; Sick Leave (SL) may involve a form or an email to the HOD, followed by completing the form and submitting it to the clerk. The exact SL sequence is not yet clear. Non-Earned Leave (NEL) and Earned Leave (EL) were identified as additional categories, but their specific application steps were not confirmed. Faculty are expected to arrange cover for classes affected by leave, often by asking a suitable colleague or subject faculty member.

The proposed solution is a **Faculty Leave & Smart Class-Coverage Tracker**. It provides a structured request, visible statuses, a timetable-based shortlist of potentially free faculty, proposed-replacement acceptance, and a clear review/decision trail. The existing approval authority and exact handoffs still need confirmation, so the coordinator and HOD steps in the prototype are proposed workflow roles rather than verified descriptions of current policy. The prototype does not automatically approve leave. A person shown as free in synthetic timetable data is only a candidate: suitability, workload, willingness and confirmation still require human review.

## 2. Scope and evidence status

- **Reported verbally by a faculty member on 24 October 2026:** CL uses a Google Form, followed by printing, signing and submitting a hard copy to the clerk. For SL, the reported route is a form or email to the HOD, followed by completing the form and submitting it to the clerk; the exact sequence needs clarification. NEL and EL exist as leave categories, but their application steps were not provided. Faculty arrange cover for each affected class, commonly by asking a suitable colleague or subject faculty member.
- **Reported verbally:** leave balance has been checked using a payslip or an HOF portal; the student has chosen not to rely on HOF details because its operation is not understood. This report therefore does not analyse or propose integration with that portal.
- **Supplied timetable evidence:** image of one section's weekly timetable with days and S1–S9 columns. S5 appears to be the lunch period; exact clock times are not provided.
- **Supplied subject-to-faculty mapping:** OS—Faculty A; PS-2—Faculty B; COA—Faculty C; WET—Faculty D; SC—Faculty E; ICP—Faculty F. This mapping is student-supplied and not independently validated.
- **Assumptions for prototype only:** additional section timetables (Sections B–J), staff assignments beyond the supplied mapping, availability, demo leave balances, request records and example cases are synthetic. No real faculty leave balance or confidential data is included.
- **Not confirmed:** the exact SL sequence; NEL/EL application procedures; who checks/records leave balance; approval authority and order; how cover acceptance is confirmed; exception handling; common-problem frequency; and actual time spent. No assumption is made about HOF portal behavior or LoP policy.

## 3. Current-state workflow (provisional)

1. Faculty member needs leave and selects the relevant category.
2. **CL (reported):** faculty completes a Google Form, prints it, signs the copy and submits it to the clerk.
3. **SL (reported, sequence unclear):** faculty may complete a form or email the HOD, then complete the form and submit it to the clerk. Confirm the exact order before treating this as a definitive flow.
4. **NEL/EL:** these categories were reported as available, but their application procedures were not provided and remain unknown.
5. For each leave, faculty arrange cover for affected classes, often by asking a suitable colleague or subject faculty member.
6. The exact approval sequence, leave-balance verification step, cover-confirmation method, decision record and notification process are **not confirmed** and must not be invented in the current-state map.

### Potential problem statement

The process spans leave-balance checks, class-cover coordination, work checks and authorization. If these are tracked separately, it may be difficult to see what is complete, which classes still need coverage, and whether a decision has been recorded. The investigation must establish whether these difficulties occur, their frequency, and their impact before describing them as confirmed problems.

## 4. Proposed solution and workflow

1. **Faculty submits a structured request:** category (CL/SL/NEL/EL), date(s), affected section/class periods, and any fields required by confirmed policy. The prototype is a proposed alternative to repeated paper handling, not a claim that all existing forms have identical fields.
2. **Basic validation:** require mandatory fields and flag a possible duplicate for human review; do not silently reject or merge requests.
3. **Leave-policy check:** show a reminder that the authorized leave-balance/policy check must occur. Because the current balance-verification and approval procedure is not confirmed, the prototype must not calculate real entitlements, integrate with HOF, or automatically convert a category to LoP.
4. **Find cover candidates:** compare the affected section timetable with the synthetic schedules for other sections; exclude the requester and anyone assigned elsewhere in that period. Missing or synthetic timetable data means availability is unverified, not guaranteed free.
5. **Confirm suitability and willingness:** the candidate is only proposed until they accept; subject suitability, workload and any college rules require human review.
6. **Handover/checks:** capture relevant handover notes if required. Do not make completion of assigned work a hard approval rule unless the college confirms it.
7. **Authorized review and decision:** route the request to the person(s) authorized under college policy. Coordinator verification and HOD final approval are proposed design options, not confirmed current policy; configure them only after validation.
8. **Notify and close:** display status and communicate the decision/coverage details to relevant people; a real implementation should retain an audit trail.
9. **Fallback:** if the tracker is unavailable or no suitable replacement is found, use the college's existing authorized manual procedure and keep the request marked pending until resolved.

## 5. Three human roles

- **Faculty:** submit/correct request; identify affected classes; view status; provide handover information.
- **Department Coordinator / Department Authorization:** verify completeness, coordinate/record cover confirmation, and check policy evidence within delegated authority. This role is a proposal; confirm whether such a role exists or whether the department/HOD performs these checks directly.
- **HOD:** retains final approval/rejection authority.

The tracker is software, not a fourth human role. It validates fields, flags duplicates and timetable conflicts, calculates a candidate shortlist, and displays status. A real implementation requires authenticated accounts, server-side role permissions, least-privilege access, an audit log, and privacy controls. The included prototype only simulates role selection and is not secure access control.

## 6. Status model

`Draft` → `Submitted` → `Needs Information` (if incomplete) → `Coverage Pending` → `Department Verification` → `Ready for HOD Review` → `Approved` or `Rejected` → `Closed/Notified`.

`Cancelled` can be added only under a defined cancellation rule. Possible duplicates are flagged for human review rather than silently merged or rejected. If no candidate is free, the request remains `Coverage Pending` and requires manual escalation. Statuses are proposed, not confirmed college terminology.

## 7. Timetable and candidate-selection logic

The supplied section timetable is used as Section A for demonstration only. The image's S1–S4 and S6–S9 are treated as teaching periods; S5 is treated as lunch. Exact start/end times are not known. Supplied subject mapping: OS—Faculty A; PS-2—Faculty B; COA—Faculty C; WET—Faculty D; SC—Faculty E; ICP—Faculty F. All additional staff assignments and Sections B–J are synthetic weekly schedules; they must never be represented as actual college timetables.

Candidate logic: for the selected day and period, collect assignments across the demo schedules; exclude the requester and anyone teaching another modeled class in that period. The remaining staff are shown as *potentially free in synthetic data only*. The candidate must accept, and an authorized person must check subject suitability, workload and local rules. Since real faculty timetables were not obtained, the demo cannot establish actual availability. Missing or synthetic timetable data means availability is unverified, not guaranteed free.

## 8. Five synthetic acceptance tests

| Case | Input | Expected behavior |
|---|---|---|
| Normal request | Required fields complete; candidate accepts; checks complete | Coordinator can verify; request becomes Ready for HOD Review; no auto-approval |
| Missing information | Leave date or affected class missing | Set Needs Information and tell requester what is missing |
| Duplicate | Same requester/date/period appears to overlap an existing request | Flag possible duplicate for human review; preserve both records until resolved |
| Unauthorized request | A user attempts to submit a request for another faculty member or a non-faculty role attempts submission | Block the attempt in the demo; a production system must enforce requester identity and permissions on the server |
| No cover / failed step | No candidate appears free, or tracker becomes unavailable | Keep coverage pending; use authorized manual fallback; reconcile records after recovery |

The Review checks page executes seven client-side assertions: normal form validation, missing date, duplicate detection, unauthorized-request blocking, no-cover fallback, non-HOD decision blocking, and weekend-date rejection for the weekday-only synthetic timetable. All seven passed in the demo checks on 24 October 2026. These are front-end rule assertions, not server-side security. In a manual browser walkthrough after the final replacement/message updates, the student verified the normal path: create a request, select and record Ananya Rao, send a message, record simulated acceptance, forward through Department Review, record HOD approval, and see the `LEAVE APPROVED` notice and HOD note after returning to the faculty account. A rejection-with-reason path is documented in the test log; recheck it in the final UI if time permits. These tests demonstrate the prototype only, not real college operations. See `tests/test-results.csv`.

## Evidence-based limitations after faculty discussion (23 October 2026)

The student reports that, during a verbal discussion on 23 October 2026, a faculty member described the faculty leave process as manual and explained that a digital system could make it easier. The faculty member also highlighted that arranging replacement faculty can sometimes be difficult because staff need to call colleagues and obtain confirmation of their availability.

The faculty member described the CL, SL, NEL and EL leave categories and shared information about the CL and SL procedures. This was a verbal report, not a direct observation or an official policy docum. The precise SL sequence, NEL/EL application steps, approval order, leave-balance verification procedure and handling of exceptions remain unknown. The report does not analyse the HOF portal or claim that it is a verified system dependency.

No actual request volume, coordination duration, delay rate or measured time savings have been collected. The prototype therefore demonstrates a proposed digital workflow using synthetic timetables and balances. Although the verbal feedback supports exploring a centralized replacement-request and confirmation process, further validation is needed to establish the scale of the problem and whether the proposed system would improve efficiency or comply with official college policy.
## 9. Benefits and measurement plan

Expected benefits to test: fewer repeated calls/messages, quicker identification of candidate cover, fewer untracked requests, clearer pending status, and fewer avoidable timetable conflicts. No measured benefit is claimed yet. The actual number of monthly requests and frequency of coordination problems were not provided. To show potential scale without inventing college volume, the calculation file includes sensitivity examples at 5, 10 and 20 requests/month: using the hypothetical 10-minute per-request saving, these scenarios correspond to 50, 100 or 200 staff-minutes per month. These are illustrative scenario volumes, not estimates of the college's actual request count.

Collect a small, permission-based sample of anonymized process observations. For each case record only start/end time or estimated active staff-minutes, number of follow-ups, whether coverage was found first try, missing details, and time spent by the coordinator/HOD. Do not collect names, student IDs, personal medical details, or confidential messages. Compare the baseline with a simulated/prototype workflow using the same cases.

`Net time saved per request = baseline active staff-minutes − proposed active staff-minutes, where proposed effort includes review and ongoing support.`

`Net time saved % = net time saved ÷ baseline active staff-minutes × 100.`

### Illustrative scenario calculation (not measured results)

To satisfy the calculation requirement without inventing an observed result, `calculations/time-savings-scenario.csv` shows an explicitly hypothetical example: baseline active staff effort = 6 minutes for application/admin + 12 minutes for finding/contacting cover + 8 minutes for clerk/coordination/review = 26 minutes per request. Proposed effort = 4 minutes for entry/admin + 5 minutes for cover search/confirmation + 5 minutes for coordinator/HOD review + 2 minutes for ongoing support/administration = 16 minutes. Scenario net saving = 26 − 16 = 10 minutes per request, or (10 ÷ 26) × 100 = 38.5%. **Every value is an illustrative assumption, not measured college data or a claim of achieved improvement.** The proposed total explicitly includes review and support effort. Replace these inputs with observed timings if they become available.

## 10. Risks, safeguards and fallback

- Incorrect or incomplete timetable can wrongly label staff as free; show data coverage and treat missing data as unknown.
- Candidate availability does not imply consent or subject suitability; require confirmation and human review.
- Leave rules may differ by category; configure only after authorized verification.
- Personal leave information is sensitive; restrict access and avoid collecting medical details beyond what official policy requires.
- HOD approval must remain with the authorized HOD; never infer or auto-approve.
- On failure, use the existing authorized manual process and reconcile afterward.

## 11. Evidence log

The evidence log template separates source, date, evidence type, claim supported, confidence, and follow-up. The timetable image and student-reported process are not equivalent to direct observation of the complete workflow. Update the log after speaking with faculty; if a claim cannot be confirmed, keep it marked unknown or remove it.

## 12. AI-use and contribution record

AI assistance was used to structure the workflow, draft the report, propose synthetic test cases, and help build and revise the demonstration prototype.

**Student contribution:** selected the faculty leave process as the case study; obtained and relayed a verbal description of the CL/SL process and the CL/SL/NEL/EL categories; supplied the Section A timetable and subject-to-faculty mapping used as initial demo input (faculty names are anonymised as Faculty A–F in this repository); decided not to rely on undocumented HOF behavior; specified interface requirements, reviewed the proposed dashboard changes, and personally ran the end-to-end browser walkthrough on 24 October 2026.

Synthetic schedules, leave balances, demo caps, test cases and time-saving inputs were created for demonstration and were not copied from actual staff records. AI assistance is disclosed above.

## 13. Evidence and limitation summary

- Source: one verbal report (24 October 2026), recorded without naming the individual. Formal permission and any request-volume or timing data were not obtained.
- Exact SL sequence, NEL/EL steps, approval order, leave-balance and cover-confirmation rules, and LoP policy are unknown and are not assumed. HOF portal behaviour is excluded.
- All other timetables, balances, caps and time-saving inputs are synthetic or assumed and are labelled as such.
- Test results are in `tests/`; section 8 states their scope limits.


## 14. Final prototype implementation and verification

The HTML demo provides Faculty, Department Coordinator and HOD views; a calendar date input; a proposed-replacement shortlist based on synthetic timetable fixtures; a replacement message/acceptance simulation; coordinator forwarding; HOD approval/rejection with a required rejection reason; and a faculty-facing decision notification. The user manually verified the successful approval path and confirmed the selected replacement remained synchronized with Coverage Messages. Seven front-end rule assertions passed. Test cases and results are recorded in `tests/`.

The prototype stores one request in page memory only. Reloading the browser clears it. Demo accounts are not secure authentication, role checks are not server-enforced, messages are not real delivery, and no database or official leave approval exists. Calendar display is browser-dependent. All category caps/balances and Sections B–J are synthetic. The prototype must not be used to determine actual leave eligibility or actual faculty availability.

