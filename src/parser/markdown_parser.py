import re

from src.models.spec import (
    FeatureSpecification,
)

def parse_markdown(
    content: str,
) -> FeatureSpecification:

    def extract(
        heading: str,
    ) -> str:

        pattern = (
            rf"# {heading}(.*?)(?=\n# |\Z)"
        )

        match = re.search(
            pattern,
            content,
            re.S,
        )

        if not match:
            return ""

        return match.group(1).strip()

    return FeatureSpecification(
        feature_objective=extract(
            "Feature Objective"
        ),
        user_story=extract(
            "User Story"
        ),
        business_rules=[
            line.strip("- ")
            for line in extract(
                "Business Rules"
            ).splitlines()
            if line.strip()
        ],
        acceptance_criteria=[
            line.strip("- ")
            for line in extract(
                "Acceptance Criteria"
            ).splitlines()
            if line.strip()
        ],
        non_functional_requirements=[
            line.strip("- ")
            for line in extract(
                "Non-Functional Requirements"
            ).splitlines()
            if line.strip()
        ],
    )