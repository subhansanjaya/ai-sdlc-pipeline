import json

from src.models.spec import (
    FeatureSpecification,
)

def parse_json(
    content: str,
) -> FeatureSpecification:

    data = json.loads(
        content
    )

    return FeatureSpecification(
        **data
    )