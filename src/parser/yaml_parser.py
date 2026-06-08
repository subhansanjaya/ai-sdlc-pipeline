import yaml

from src.models.spec import (
    FeatureSpecification,
)

def parse_yaml(
    content: str,
) -> FeatureSpecification:

    data = yaml.safe_load(
        content
    )

    return FeatureSpecification(
        **data
    )