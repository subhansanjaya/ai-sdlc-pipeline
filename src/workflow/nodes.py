"""
LangGraph workflow nodes.

Each node represents a stage in the AI SDLC workflow.

Flow:

Specification
    ↓
Planning
    ↓
Approval Gate
    ↓
Implementation
    ↓
Test Generation

The nodes are responsible for:
- Generating artefacts
- Persisting artefacts
- Updating shared workflow state
"""

from langgraph.types import (
    interrupt,
)

from src.workflow.state import (
    PipelineState,
)

# Planning services
from src.services.planning_service import (
    create_plan,
)
from src.services.plan_storage import (
    save_plan,
)

# Implementation services
from src.services.implementation_service import (
    generate_implementation,
)
from src.services.code_storage import (
    save_code,
)
from src.services.change_summary import (
    create_summary,
)

# Test generation services
from src.services.test_generation_service import (
    generate_tests,
)
from src.services.test_storage import (
    save_tests,
)
from src.services.traceability import (
    generate_traceability,
)


def planning_node(
    state: PipelineState,
) -> PipelineState:
    """
    Generate and persist an implementation plan.

    Input:
        Specification

    Output:
        Updated workflow state containing
        the implementation plan.
    """

    plan = create_plan(
        state["spec"]
    )

    # Persist plan for traceability
    # and downstream manual execution.
    save_plan(
        plan
    )

    state["plan"] = plan

    return state


def approval_node(
    state: PipelineState,
) -> PipelineState:
    """
    Human approval gate.

    LangGraph pauses execution and stores
    workflow state in SQLite.

    The workflow may later resume with:

    approve
    reject
    """

    decision = interrupt(
        {
            "message":
                "Approve implementation?",
            "choices": [
                "approve",
                "reject",
            ],
        }
    )

    if decision == "reject":

        raise ValueError(
            "Implementation rejected"
        )

    return state


def implementation_node(
    state: PipelineState,
) -> PipelineState:
    """
    Generate implementation code from the
    specification and implementation plan.

    The generated code is persisted and
    attached to workflow state.
    """

    if state["plan"] is None:

        raise ValueError(
            "Plan must exist before implementation"
        )

    code = generate_implementation(
        state["spec"],
        state["plan"],
    )

    # Persist generated code.
    save_code(
        "order_sorting.py",
        code,
    )

    # Generate simple change summary.
    create_summary(
        "order_sorting.py"
    )

    state["code"] = code

    return state


def test_node(
    state: PipelineState,
) -> PipelineState:
    """
    Generate tests from the specification
    and implementation plan.

    The generated tests are persisted and
    traceability information is produced.
    """

    if state["plan"] is None:

        raise ValueError(
            "Plan must exist before test generation"
        )

    tests = generate_tests(
        state["spec"],
        state["plan"],
    )

    # Persist generated tests.
    save_tests(
        tests
    )

    # Create acceptance criteria
    # traceability mapping.
    generate_traceability(
        state["spec"]
    )

    state["tests"] = tests

    return state