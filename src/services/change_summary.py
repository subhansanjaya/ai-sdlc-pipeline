from pathlib import Path

def create_summary(
    filename: str,
) -> None:

    summary = f"""
# Generated Changes

Generated File:

- {filename}

Reason:

Created from approved
feature specification
and implementation plan.
"""

    Path(
        "generated/change_summary.md"
    ).write_text(
        summary
    )