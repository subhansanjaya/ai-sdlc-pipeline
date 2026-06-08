from pathlib import Path

def save_tests(
    content: str,
) -> None:

    Path(
        "generated/tests"
    ).mkdir(
        parents=True,
        exist_ok=True,
    )

    Path(
        "generated/tests/test_generated.py"
    ).write_text(
        content
    )