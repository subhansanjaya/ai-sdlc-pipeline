from fastapi import APIRouter

from .schemas import PipelineRequest, PipelineResponse
from src.services.workflow_service import WorkflowService

router = APIRouter()

workflow_service = WorkflowService()


@router.get("/")
def root() -> dict[str, str]:
    """
    Root endpoint.
    """
    return {
        "message": "AI SDLC Pipeline API"
    }


@router.get("/health")
def health() -> dict[str, str]:
    """
    Health check endpoint.
    """
    return {
        "status": "healthy"
    }


@router.post(
    "/pipeline/run",
    response_model=PipelineResponse,
)
def run_pipeline(
    request: PipelineRequest,
) -> PipelineResponse:
    """
    Execute the AI SDLC workflow from a specification file.
    """

    return workflow_service.run_from_path(
        request.path
    )