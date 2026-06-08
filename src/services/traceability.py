import json
from pathlib import Path

from src.models.spec import (
    FeatureSpecification,
)


def generate_traceability(
    spec: FeatureSpecification,
) -> None:

    matrix = {}

    for index, criterion in enumerate(
        spec.acceptance_criteria,
        start=1,
    ):
        matrix[
            f"AC{index:03}"
        ] = {
            "acceptance_criteria": criterion,
            "test_file":
                "generated/tests/test_generated.py",
        }

    Path(
        "generated/traceability.json"
    ).write_text(
        json.dumps(
            matrix,
            indent=2,
        )
    )