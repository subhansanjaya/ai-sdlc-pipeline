from pathlib import Path
from src.models.plan import ImplementationPlan

def load_plan() -> ImplementationPlan:

    content = Path(
        "generated/plans/plan.json"
    ).read_text()

    return (
        ImplementationPlan
        .model_validate_json(
            content
        )
    )