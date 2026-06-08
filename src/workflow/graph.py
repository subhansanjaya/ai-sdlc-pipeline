from langgraph.graph import (
    StateGraph,
    END,
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

graph = StateGraph(
    PipelineState
)

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

graph.set_entry_point(
    "plan"
)

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

# workflow = graph.compile()

from langgraph.checkpoint.sqlite import (
    SqliteSaver,
)

import sqlite3

conn = sqlite3.connect(
    "workflow.db",
    check_same_thread=False,
)

checkpointer = SqliteSaver(
    conn
)

workflow = graph.compile(
    checkpointer=checkpointer
)