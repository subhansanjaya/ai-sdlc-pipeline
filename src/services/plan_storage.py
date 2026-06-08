# import json
from pathlib import Path
from src.models.plan import ImplementationPlan

def save_plan(
    plan: ImplementationPlan,
) -> None:

    Path(
        "generated/plans"
    ).mkdir(
        parents=True,
        exist_ok=True,
    )

    Path(
        "generated/plans/plan.json"
    ).write_text(
        plan.model_dump_json(
            indent=2
        )
    )