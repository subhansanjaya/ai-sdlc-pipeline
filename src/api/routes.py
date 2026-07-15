from fastapi import APIRouter
from .schemas import PipelineRequest, PipelineResponse

# from src.services.pipeline_service import PipelineService
from src.services.workflow_service import WorkflowService
from src.services.spec_service import load_spec
# from typing import Any
# pipeline_service = PipelineService()

router = APIRouter()
workflow_service = WorkflowService()

@router.get("/")
def root() -> dict[str, str]:
    return {
        "message": "AI SDLC Pipeline API"
    }


@router.get("/health")
def health() -> dict[str, str]:
    return {
        "status": "healthy"
    }

# @router.post("/pipeline/run")
# def run_pipeline(request: PipelineRequest):

#     return pipeline_service.run(request)
@router.post("/pipeline/run")
def run_pipeline(request: PipelineRequest) -> PipelineResponse:

    spec = load_spec(request.path)

    result = workflow_service.run(spec)

    return result