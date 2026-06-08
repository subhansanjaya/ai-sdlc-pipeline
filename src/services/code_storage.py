from pathlib import Path

from src.services.file_guard import (
    validate_path,
)

def save_code(
    filename: str,
    content: str,
) -> None:

    path = (
        f"generated/code/{filename}"
    )

    validate_path(path)

    Path(
        "generated/code"
    ).mkdir(
        parents=True,
        exist_ok=True,
    )

    Path(path).write_text(
        content
    )