from src.models.plan import (
    ImplementationPlan,
)

from src.services.audit_service import (
    write_audit_record,
)

def audit_plan(
    plan: ImplementationPlan,
) -> None:

    write_audit_record(
        "plan_generated",
        plan.model_dump(),
    )