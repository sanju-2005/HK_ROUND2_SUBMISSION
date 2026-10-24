# Proposed lab/capstone: Faculty Leave and Class-Coverage Workflow

## Why this project fits the audit

Task 1 investigates the college's manual faculty-leave workflow. This proposal reuses that workflow as a small software-engineering and AI/data-systems capstone, so the same problem can be studied twice from different angles: Task 1 evaluates the process and controls; Task 2 proposes a curriculum-aligned project to implement and test a safer workflow. This is a student proposal, not a live IFHE system.

## Problem statement

A manual leave process can require a request, completeness check, approval, class-cover decision, notification and closure. Until the actual process is confirmed, these are a proposed process model rather than claims that every step currently occurs at IFHE.

## Minimum viable scope

- Accept a synthetic leave request with staff alias, dates, reason category, affected class slots and supporting-document flag; never use real staff/student details in the demo.
- Track states: `Draft`, `Submitted`, `Needs information`, `Pending approval`, `Approved`, `Rejected`, `Class cover pending`, `Covered`, `Closed`, `Failed/manual review`.
- Validate required fields and date ranges; flag duplicate requests using a stable request key; enforce role-based actions.
- Keep approval authority separate from request submission; a simulated approver can approve/reject but cannot alter the original requester's identity.
- Generate a class-cover checklist and status trail; do not automatically promise a substitute lecturer or make policy decisions.
- Provide an exception queue for notification failure, unavailable approver, conflicting timetable slot or incomplete data. The fallback is a manual coordinator review.

## Example synthetic acceptance tests

| Case | Input | Expected behavior | Recovery/control |
|---|---|---|---|
| Normal | Complete request, authorised requester, valid dates | `Submitted` → `Pending approval`; after approval, `Class cover pending` → `Covered` → `Closed` | Record timestamps and approver action; notify requester with synthetic receipt |
| Missing information | End date missing | Move to `Needs information`; do not submit for approval | Return missing field list; allow requester to amend and resubmit |
| Duplicate | Same requester/date range/class key sent twice | Detect second request and show existing request ID; do not create duplicate workflow | Allow reviewer to confirm genuinely distinct case or keep duplicate blocked |
| Unauthorized request | User without requester/approver role attempts action | Reject action and record an access-denied event | Keep request unchanged; route genuine access issue to administrator |
| Failed step | Notification service mocked as unavailable after approval | Approval remains recorded; request status is not rolled back silently | Retry notification; if retry fails, flag manual follow-up and preserve audit trail |

## How to assess it

Deliverables: workflow diagram, requirements, state-transition table, role/approval matrix, synthetic test report, simple interactive or CLI prototype, test data, README, known limitations and a short demo. Suggested rubric: workflow correctness 20%; validation/permissions 20%; five-case test evidence 20%; recovery and traceability 15%; code quality/reproducibility 10%; privacy/limitations 10%; explanation 5%.

## Curriculum mapping

- CS101/CS201: functions, modular design and validation.
- CS102/CS203: duplicate detection and state-transition logic.
- CS206: request/status schema and safe updates.
- CS205/DS202: form or API and application structure.
- CS307: optional deployment/logging.
- SP301/Internship: end-to-end tests, documentation, demo and evaluation.
- DS408/NLP (optional): extract or answer from policy text only if approved documents can be used lawfully; otherwise use synthetic text and show source grounding.

## Safety and limitations

Use only synthetic data. This project does not access a live college service, does not decide leave eligibility, and does not replace the official approver. Any production deployment would require institution permission, access-control design, privacy review, audit retention rules, accessibility checks and integration approval.
