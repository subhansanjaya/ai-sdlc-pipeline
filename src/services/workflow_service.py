import uuid

from langchain_core.runnables import RunnableConfig

from src.api.schemas import PipelineResponse
from src.models.spec import FeatureSpecification
from src.services.spec_service import load_spec
from src.workflow.graph import workflow
from src.workflow.state import PipelineState


class WorkflowService:
    """
    Service responsible for executing the AI SDLC LangGraph workflow.
    """

    def run(
        self,
        spec: FeatureSpecification,
        thread_id: str | None = None,
    ) -> PipelineResponse:
        """
        Execute the workflow using an already loaded specification.
        """

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

        status = (
            "waiting_for_approval"
            if "__interrupt__" in result
            else "completed"
        )

        return PipelineResponse(
            thread_id=thread_id,
            status=status,
        )

    def run_from_path(
        self,
        path: str,
        thread_id: str | None = None,
    ) -> PipelineResponse:
        """
        Load a specification from disk and execute the workflow.
        """

        spec = load_spec(path)

        return self.run(
            spec=spec,
            thread_id=thread_id,
        )