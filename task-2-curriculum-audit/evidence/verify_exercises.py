"""Small reproducible checks for the CS101 and CS102 AI-assisted examples.

Run with: python evidence/verify_exercises.py
This is a learning check, not exhaustive or production-grade testing.
"""


def score_band(score):
    if isinstance(score, bool) or not isinstance(score, (int, float)):
        raise TypeError("score must be numeric")
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")
    return "pass" if score >= 40 else "fail"


def unique_preserving_order(items):
    return list(dict.fromkeys(items))


def expect_exception(function, expected_type):
    try:
        function()
    except expected_type:
        return
    except Exception as exc:  # pragma: no cover - diagnostic branch
        raise AssertionError(
            f"Expected {expected_type.__name__}, got {type(exc).__name__}"
        ) from exc
    raise AssertionError(f"Expected {expected_type.__name__}, but no exception was raised")


def main():
    cs101_checks = [
        (lambda: score_band(0) == "fail", "score 0"),
        (lambda: score_band(39) == "fail", "score 39"),
        (lambda: score_band(40) == "pass", "score 40"),
        (lambda: score_band(100) == "pass", "score 100"),
        (lambda: expect_exception(lambda: score_band(-1), ValueError), "score -1 rejected"),
        (lambda: expect_exception(lambda: score_band(101), ValueError), "score 101 rejected"),
        (lambda: expect_exception(lambda: score_band("40"), TypeError), "string rejected"),
        (lambda: expect_exception(lambda: score_band(True), TypeError), "bool rejected"),
    ]
    cs102_checks = [
        (lambda: unique_preserving_order([3, 1, 3, 2, 1]) == [3, 1, 2], "duplicates removed in order"),
        (lambda: unique_preserving_order([]) == [], "empty list"),
        (lambda: unique_preserving_order([4, 5]) == [4, 5], "unique items unchanged"),
        (lambda: expect_exception(lambda: unique_preserving_order([[1], [1]]), TypeError), "unhashable items rejected"),
    ]

    total = 0
    for label, checks in (("CS101 score_band", cs101_checks), ("CS102 unique_preserving_order", cs102_checks)):
        for run_check, description in checks:
            try:
                result = run_check()
                if result is False:
                    raise AssertionError(f"Failed: {description}")
            except Exception as exc:
                raise SystemExit(f"FAIL — {label}: {description}: {exc}") from exc
        print(f"{label}: {len(checks)}/{len(checks)} checks passed")
        total += len(checks)
    print(f"All {total} code checks passed.")


if __name__ == "__main__":
    main()
