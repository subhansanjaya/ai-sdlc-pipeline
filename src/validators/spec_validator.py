from src.models.spec import (
    FeatureSpecification,
)


def validate_spec(
    spec: FeatureSpecification,
) -> None:

    if not spec.feature_objective:
        raise ValueError(
            "Feature Objective missing"
        )

    if not spec.user_story:
        raise ValueError(
            "User Story missing"
        )

    if not spec.business_rules:
        raise ValueError(
            "Business Rules missing"
        )

    if not spec.acceptance_criteria:
        raise ValueError(
            "Acceptance Criteria missing"
        )

    if (
        not spec.non_functional_requirements
    ):
        raise ValueError(
            "Non Functional Requirements missing"
        )