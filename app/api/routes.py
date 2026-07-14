from fastapi import APIRouter, HTTPException

try:
    from app.schemas.schemas import OutlineResponse, TopicRequest
    from app.services.service import generate_outline
except ModuleNotFoundError:  # pragma: no cover - supports running from the app directory
    from schemas.schemas import OutlineResponse, TopicRequest
    from services.service import generate_outline

router = APIRouter()


@router.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@router.post("/generate", response_model=OutlineResponse)
async def generate_research(request: TopicRequest):
    try:
        return generate_outline(request)
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc

