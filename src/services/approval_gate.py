from src.services.approval_loader import (
    load_approval,
)

def verify_approval(
    stage: str,
) -> None:

    approval = load_approval(
        stage
    )

    if not approval.approved:
        raise ValueError(
            f"{stage} not approved"
        )