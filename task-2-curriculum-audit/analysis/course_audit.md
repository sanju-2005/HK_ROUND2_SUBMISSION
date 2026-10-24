# Curriculum audit — provisional baseline and findings

## 1. Executive summary

The supplied portal screenshots list 50 courses over Semesters I–VII. The student reports a 15-credit internship in Semester VIII, making **51 baseline rows and 166 provisional credits** in total. The highest-credit semesters in the displayed data are Semesters II–V at 24 credits each; Semester VIII is shown as 15 credits based on the student's statement.

The curriculum already contains a substantive AI pathway: Introduction to AI and DS, Artificial Intelligence, Mathematical Essentials for ML, Machine Learning, Predictive Analytics, Deep Learning, Pattern Recognition, NLP, Computer Vision and Generative AI. It also includes important computer science foundations such as data structures, OOP, DBMS, algorithms, operating systems, networks, web technologies and cloud computing. The defensible concern is therefore not “the curriculum has no AI”; it is whether existing courses consistently teach current development practices—testing, Git workflows, data leakage prevention, model evaluation, retrieval-augmented systems, responsible AI, APIs, deployment and monitoring—and whether those outcomes are assessed in hands-on work. The screenshots show course names and credits, not detailed syllabi or assessments, so content gaps remain hypotheses to check against course outlines.

## 2. Scope, provenance and limitations

- Programme label assumed for audit framing: B.Tech CSE (Artificial Intelligence), pending confirmation of the student's registered programme title. IFHE lists CSE (AI), CSE (AI & Data Science), and CSE (AI & Machine Learning) as distinct programme options [S1, S2].
- Baseline source: student-provided portal screenshots for Semesters I–VII and student-reported Semester VIII internship value.
- The displayed course portal says “2027 Courses,” but that label alone does not establish the admission batch, scheme version or governing regulations.
- An official public IFHE structure was consulted, but its codes/semester placement/credits do not exactly match the screenshots; it has therefore not been silently substituted for the student's course list.
- No detailed course outcomes, lab manuals, assessment rubrics, official regulations or faculty review were available at drafting time.
- This is a student-led proposal, not an official IFHE syllabus revision.

## 3. Baseline credits

| Semester | Credits from screenshot/student report |
|---|---:|
| I | 20 |
| II | 24 |
| III | 24 |
| IV | 24 |
| V | 24 |
| VI | 19 |
| VII | 16 |
| VIII internship | 15 |
| **Total** | **166** |

Calculation: 20 + 24 + 24 + 24 + 24 + 19 + 16 + 15 = 166. Zero-credit HS101 is included as a course row but contributes zero credits.

## 4. What appears strong in the baseline

1. **Broad AI coverage:** AI, ML, predictive analytics, deep learning, pattern recognition, NLP, computer vision and GenAI appear as distinct courses.
2. **Core CS foundation:** programming, data structures, OOP, DBMS, algorithms, architecture, operating systems, networks, web technologies and cloud are present.
3. **Math foundations:** linear algebra/ODEs, higher calculus, discrete mathematics and mathematical essentials for ML are represented. Probability/statistics did not appear in the supplied seven-semester screenshots; confirm whether it is present in another course, transfer credit or a different curriculum version before calling it absent.
4. **Experiential learning:** Special Project and Internship offer potential vehicles for integrated work; the assessment criteria and expected artifacts are not yet verified.

## 5. Evidence-driven gap hypotheses

The dated postings reviewed mention code/version control, data/SQL, model evaluation, RAG/LLM evaluation, APIs, deployment, cloud, privacy and reliability [S3–S5]. The course titles suggest places to assess these topics, but do not prove they are absent. The recommendations below are design proposals, not claims that current faculty omit the topics. For the quantified redesign calculation, the core update scope is CS101, CS102, CS201, CS203, CS206, DS202, DS304 and DS305, plus the four conditional reduction candidates. Rows 6–8 are retain decisions with optional ideas for a later syllabus review; they are not counted in the 41-credit core-scope figure.

## 6. Twelve course decisions

| # | Decision | Course(s) | Specific proposed change and rationale | Evidence / check |
|---:|---|---|---|---|
| 1 | UPDATE (keep courses; revise assessed work) | CS102 Data Structures; CS203 Design and Analysis of Algorithms | Retain both core courses but make tested coding exercises, time/space-complexity explanations and edge-case evidence explicit in assessed work. | Baseline includes both; job sample supports programming and problem-solving skills [S3, S4]. Check present assessment rubrics before asserting a gap. |
| 2 | UPDATE | CS101 Computer Programming; CS201 OOP | Assess functions, modular design, exception handling, unit tests, readable code and Git basics across labs. | Junior AI/ML role lists Python and Git as must-have [S3]. Exact programming language/outcomes must be verified. |
| 3 | UPDATE | CS206 DBMS; DS305 Data Wrangling and Visualization | Add robust SQL tasks, schema/data validation, missing-value handling, provenance and leakage-safe train/test preparation. | SQL is listed [S3]; data-rich AI role emphasizes traceable scientific systems [S5]. |
| 4 | UPDATE | DS202 Industry Coding Practice | Use Git branches/commits, code review, tests, CLI and API consumption as assessable deliverables, not optional tool use. | Git and software validation are explicit in [S3]. |
| 5 | UPDATE DS304; KEEP DS310 | DS304 Machine Learning; DS310 Predictive Analytics | In Machine Learning, assess a baseline, correct data splits, suitable metrics, error analysis and reproducible experiment notes. Retain Predictive Analytics pending review of its detailed syllabus. | Model training/evaluation appears in [S3, S5]; validate existing labs before claiming a gap. DS304 is counted in the core scope; DS310 is not. |
| 6 | KEEP | DS306 Deep Learning; CS305 Computer Vision | Retain both specialist AI courses. Data handling, baseline comparison and reproducible inference are useful future assessment-check ideas, but no course-level change is included for these courses in the quantified scope. | AI/ML and vision-related work appears in [S4, S5]; Wipro and Amgen seniority caveats apply. Check the actual course outlines first. |
| 7 | KEEP | DS311 Natural Language Processing; DS408 Generative AI | Retain the existing NLP and GenAI courses. Use the separate proposed Responsible GenAI Product Lab for a small applied demonstration; deeper changes to these courses are outside the quantified core scope. | RAG, vector databases and LLM evaluation appear in [S3]; Amgen [S5] is used only as a senior-role signal for robustness and responsible use. |
| 8 | KEEP | CS307 Cloud Computing; SP301 Special Project; Internship | Retain their existing credit allocations. A deployable prototype and recovery demonstration could be proposed in a future course-owner review, but these courses are not counted in the 41-credit core scope. | APIs/cloud are mentioned in [S3, S4]; [S5] discusses reproducible deployment and documentation in a senior scientific role. |
| 9 | ADD (1 credit) | New: Software Testing, Git and API Basics (Semester V) | Practical mini-course for unit tests, Git workflow, API requests, error handling, idempotency and code review. | Repeated software engineering signals across [S3, S4]. Prerequisite should be programming/OOP; credits subject to approval. |
| 10 | ADD (1 credit) | New: MLOps and Model Deployment (Semester VI) | Cover model packaging, environment/version control, deployment smoke tests, drift/monitoring concepts and rollback. | Cloud/deployment and model evaluation signals [S3–S5]. Prerequisites: ML and coding practice. |
| 11 | ADD (2 credits) | New: Responsible GenAI Product Lab (Semester VII) | Build a small retrieval-backed assistant with source display, evaluation cases, privacy note, access controls and failure handling. | [S3] lists RAG, vector databases and LLM evaluation; [S5] adds robustness, bias, uncertainty and responsible-use concerns in a senior scientific role. Prerequisites: NLP/GenAI and coding practice. |
| 12 | REDUCE / convert to flexible elective (conditional) | DS303 Blockchain Technology; EC308 Embedded Systems; OE418 VR/AR Systems; OE801 English for Competitive Exams | Proposed 3→2 credits each only if official regulations, programme outcomes and existing syllabi allow it. Use the freed 4 credits to create the three practical modules above (1+1+2). Do not remove compulsory learning by assumption. | The job sample offers less direct evidence for these topics than for implementation/evaluation skills, but limited job sample is not proof these courses lack value. Obtain curriculum-owner approval and preserve legitimate career pathways. |

## 7. Eight-to-twelve reasoning count

The table provides twelve actionable decisions, including keep decisions as well as updates, additions and conditional reductions. The quantified core intervention affects eight existing courses by changing assessed outcomes and conditionally reviews four other courses for credit transfer. For a final interview, explain the evidence and trade-offs; do not claim a course lacks content unless an official syllabus or assessment artifact supports that claim.

## 8. Stakeholder feedback

No faculty or graduate feedback has been collected for this draft as of 23 October 2026. Because the deadline is close, this report records the gap rather than implying consultation happened.

## 9. Conclusion

The recommended approach is to preserve the existing AI and CS foundation while making practical engineering outcomes more explicit: tested code, reliable data handling, reproducible model evaluation, grounded GenAI, API integration, deployment and recovery. Proposed reductions are conditional and must not be read as an official recommendation to eliminate subject value before prerequisite and regulation checks.
