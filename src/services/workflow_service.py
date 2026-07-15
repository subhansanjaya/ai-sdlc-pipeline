import uuid

from langchain_core.runnables import RunnableConfig

from src.workflow.graph import workflow
from src.workflow.state import PipelineState
from src.models.spec import FeatureSpecification


class WorkflowService:

    def run(
        self,
        spec: FeatureSpecification,
        thread_id: str | None = None,
    ):

        if thread_id is None:
            thread_id = str(uuid.uuid4())

        config: RunnableConfig = {
            "configurable": {
                "thread_id": thread_id,
            }
        }

        initial_state: PipelineState = {
            "spec": spec,
            "plan": None,
            "code": None,
            "tests": None,
        }

        result = workflow.invoke(
            initial_state,
            config=config,
        )

        return {
            "thread_id": thread_id,
            "status": (
                "waiting_for_approval"
                if "__interrupt__" in result
                else "completed"
            ),
            "result": result,
        }