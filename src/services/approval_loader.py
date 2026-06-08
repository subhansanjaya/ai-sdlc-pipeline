from pathlib import Path

from src.models.approval import (
    Approval,
)

def load_approval(
    stage: str,
) -> Approval:

    path = Path(
        f"generated/approvals/{stage}.json"
    )

    if not path.exists():
        raise ValueError(
            f"Approval not found for stage: {stage}"
        )

    return Approval.model_validate_json(
        path.read_text()
    )