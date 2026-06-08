from src.workflow.state import (
    PipelineState,
)

from src.services.planning_service import (
    create_plan,
)

from src.services.implementation_service import (
    generate_implementation,
)

from src.services.test_generation_service import (
    generate_tests,
)

def planning_node(
    state: PipelineState,
) -> PipelineState:

    state["plan"] = create_plan(
        state["spec"]
    )

    return state


def implementation_node(
    state: PipelineState,
) -> PipelineState:

    if state["plan"] is None:
        raise ValueError(
            "Plan must exist before implementation"
        )

    state["code"] = generate_implementation(
        state["spec"],
        state["plan"],
    )

    return state


def test_node(
    state: PipelineState,
) -> PipelineState:

    if state["plan"] is None:
        raise ValueError(
            "Plan must exist before test generation"
        )

    state["tests"] = generate_tests(
        state["spec"],
        state["plan"],
    )

    return state

# def approval_node(
#     state: PipelineState,
# ) -> PipelineState:

#     interrupt(
#         {
#             "message":
#                 "Approve implementation?"
#         }
#     )

#     return state

def approval_node(
    state: PipelineState,
) -> PipelineState:

    answer = input(
        "Approve implementation? (y/n): "
    )

    if answer.lower() != "y":
        raise ValueError(
            "Implementation rejected"
        )

    return state