import sqlite3

from langgraph.checkpoint.sqlite import (
    SqliteSaver,
)

from langgraph.graph import (
    END,
    StateGraph,
)

from src.workflow.state import (
    PipelineState,
)

from src.workflow.nodes import (
    planning_node,
    approval_node,
    implementation_node,
    test_node,
)


# Create workflow graph using the shared
# PipelineState object.
graph = StateGraph(
    PipelineState
)

# Register workflow nodes.
graph.add_node(
    "plan",
    planning_node,
)

graph.add_node(
    "approve",
    approval_node,
)

graph.add_node(
    "implement",
    implementation_node,
)

graph.add_node(
    "tests",
    test_node,
)

# Define workflow entry point.
graph.set_entry_point(
    "plan"
)

# Define workflow execution path.
graph.add_edge(
    "plan",
    "approve",
)

graph.add_edge(
    "approve",
    "implement",
)

graph.add_edge(
    "implement",
    "tests",
)

graph.add_edge(
    "tests",
    END,
)

# SQLite checkpoint persistence.
#
# LangGraph stores workflow state here,
# allowing workflows to pause, survive
# application restarts, and resume later.
conn = sqlite3.connect(
    "workflow.db",
    check_same_thread=False,
)

checkpointer = SqliteSaver(
    conn
)

# Compile workflow with checkpoint support.
workflow = graph.compile(
    checkpointer=checkpointer
)