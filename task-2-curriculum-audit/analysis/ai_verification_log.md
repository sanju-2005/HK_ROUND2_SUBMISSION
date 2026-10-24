# AI-assisted exercise log — five subjects

## How this log was made

The five prompt/output examples were prepared in this ChatGPT conversation using GPT-6 on 23 October 2026. Exercises 1 and 2 were checked in the preparation environment and the student subsequently ran `verify_exercises.py` on Windows with Python 3.14 in PowerShell. The student-pasted terminal output recorded 8/8 CS101 checks and 4/4 CS102 checks passing. Exercises 3–5 were cross-checked with AI assistance against the linked technical sources during preparation; no real dataset, trained CNN, or production retrieval system was used. The student has not independently read all three technical guides, and that limitation is disclosed rather than described as personal review.

## Exercise 1 — CS101 Computer Programming

- **Prompt:** “Write a Python function `score_band(score)` that accepts a numeric score from 0 through 100 and returns `pass` for scores >= 40 and `fail` otherwise. Reject values outside the range and non-numeric input clearly. Give test cases for boundary values and invalid values.”
- **Model/date:** ChatGPT (GPT-6), 23 October 2026.
- **Output produced:**
  ```python
  def score_band(score):
      if isinstance(score, bool) or not isinstance(score, (int, float)):
          raise TypeError("score must be numeric")
      if not 0 <= score <= 100:
          raise ValueError("score must be between 0 and 100")
      return "pass" if score >= 40 else "fail"
  ```
- **Verification method:** Boundary and invalid-input assertions were included in `verify_exercises.py`; the student ran the script locally on Windows, Python 3.14, PowerShell on 23 October 2026.
- **Actual local result pasted by student:** `CS101 score_band: 8/8 checks passed`; the same run printed `All 12 code checks passed.`
- **Checks represented:** `score_band(0) -> fail`; `score_band(39) -> fail`; `score_band(40) -> pass`; `score_band(100) -> pass`; `-1` and `101` raised `ValueError`; `'40'` and `True` raised `TypeError`.
- **Limit/correction:** Booleans are explicitly rejected because Python treats `bool` as a subclass of `int`. These are scripted test cases, not exhaustive proof for every possible input.

## Exercise 2 — CS102 Data Structures

- **Prompt:** “Write a short Python function to remove duplicate hashable items from a list while preserving first-occurrence order. Explain the data structure and test `[3, 1, 3, 2, 1]`, an empty list, and a list with all unique values. Mention a limitation.”
- **Model/date:** ChatGPT (GPT-6), 23 October 2026.
- **Output produced:** `def unique_preserving_order(items): return list(dict.fromkeys(items))`
- **Verification method:** Sample cases and a limitation case were included in `verify_exercises.py`; the student ran the script locally on Windows, Python 3.14, PowerShell on 23 October 2026.
- **Actual local result pasted by student:** `CS102 unique_preserving_order: 4/4 checks passed`; the same run printed `All 12 code checks passed.`
- **Checks represented:** `[3, 1, 3, 2, 1] -> [3, 1, 2]`; `[] -> []`; `[4, 5] -> [4, 5]`; nested/unhashable list items raised `TypeError`.
- **Limit/correction:** The implementation only supports hashable items; it is not a general deduplication method for nested lists or dictionaries.

## Exercise 3 — DS304 Machine Learning

- **Prompt:** “Explain data leakage in a supervised-learning pipeline in beginner-friendly terms. Give an incorrect preprocessing sequence and a corrected sequence, and explain how a scikit-learn Pipeline helps.”
- **Model/date:** ChatGPT (GPT-6), 23 October 2026.
- **Output summary:** Leakage occurs when information unavailable at real prediction time influences training or model selection. Split the data first, fit preprocessing on training data only, and apply the fitted transformation to held-out data. A scikit-learn Pipeline helps keep preprocessing inside training/cross-validation folds.
- **Verification method:** AI-assisted cross-check against the official scikit-learn User Guide, “Common pitfalls and recommended practices,” including sections on avoiding leakage and preprocessing: https://scikit-learn.org/stable/common_pitfalls.html (accessed 23 October 2026). The guide warns against fitting transformations using held-out test data and recommends pipelines for cross-validation/model selection.
- **Result/limitation:** The explanation matches the guide's split-first/preprocessing discipline. No dataset experiment was run. This was a source cross-check with AI assistance; the student did not independently read the full guide before this draft.

## Exercise 4 — DS306 Deep Learning

- **Prompt:** “Describe a small image-classification experiment using a CNN. Separate training, validation and test roles; explain what to log; name two ways a misleadingly high test score can happen.”
- **Model/date:** ChatGPT (GPT-6), 23 October 2026.
- **Output summary:** Train model parameters using training data; use validation data to choose model/configuration; use a held-out test set for final evaluation. Record dataset/split method, preprocessing, seed when relevant, architecture, optimizer, loss, metrics, class balance and errors. Duplicate/near-duplicate leakage or repeated test-set tuning can make scores misleadingly high.
- **Verification method:** AI-assisted cross-check against the official PyTorch tutorial, “Optimizing Model Parameters”: https://pytorch.org/tutorials/beginner/basics/optimization_tutorial.html (accessed 23 October 2026). It demonstrates training and test data loaders and separate training/evaluation loops.
- **Result/limitation:** The tutorial supports the training/evaluation distinction, but its code does not show a separate validation split. Validation and duplicate leakage are additional methodology points, not claims copied from that tutorial. No CNN was trained and no accuracy is claimed. This source cross-check used AI assistance; the student did not independently read the full tutorial before this draft.

## Exercise 5 — DS311 Natural Language Processing

- **Prompt:** “Use this synthetic mini-corpus: (D1) ‘A leave request includes a faculty member and a date range.’ (D2) ‘The Head of Department reviews a leave request.’ Answer: ‘Who reviews the leave request?’ Show the supporting sentence and explain how retrieval should be evaluated.”
- **Model/date:** ChatGPT (GPT-6), 23 October 2026.
- **Output produced:** Answer: “The Head of Department.” Supporting sentence: D2, “The Head of Department reviews a leave request.” The response also suggested evaluating retrieval on labelled question-document pairs (such as whether a relevant document appears in top-k) and evaluating answer grounding separately.
- **Verification method:** Direct text check against synthetic D2; the sentence explicitly names the reviewer. AI-assisted cross-check against the official OpenAI Retrieval guide: https://platform.openai.com/docs/guides/retrieval (accessed 23 October 2026) for retrieval and vector-store concepts.
- **Result/limitation:** The answer is grounded in the supplied sentence. One question cannot establish retrieval quality across documents/questions; a larger labelled set and a retrieval metric would be needed. No real college policy or personal data was used. The technical guide was cross-checked with AI assistance; the student did not independently read the full guide before this draft.

## Final interpretation

Two exercises have a student-run local test result (CS101 and CS102). For DS304, DS306 and DS311, the log records AI-assisted technical-source cross-checks, not independent student source reviews. No live college data, CNN training, or production retrieval evaluation is claimed.
