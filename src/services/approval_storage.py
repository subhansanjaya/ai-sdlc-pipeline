from pathlib import Path

from src.models.approval import (
    Approval,
)

from src.services.audit_service import (
    write_audit_record,
)

def save_approval(
    approval: Approval,
) -> None:

    Path(
        "generated/approvals"
    ).mkdir(
        parents=True,
        exist_ok=True,
    )

    filename = (
        f"{approval.stage}.json"
    )

    Path(
        f"generated/approvals/{filename}"
    ).write_text(
        approval.model_dump_json(
            indent=2
        )
    )

    write_audit_record(
        "approval",
        approval.model_dump(),
    )