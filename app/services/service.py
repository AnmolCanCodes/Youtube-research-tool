import json
from typing import Any

from fastapi import HTTPException

try:
    from app.llms.client import generate_outline_text
    from app.schemas.schemas import OutlineResponse, TopicRequest
except ModuleNotFoundError:  # pragma: no cover - supports running from the app directory
    from llms.client import generate_outline_text
    from schemas.schemas import OutlineResponse, TopicRequest


def _coerce_outline(payload: Any, fallback_title: str) -> OutlineResponse:
    if isinstance(payload, dict):
        data = payload
    else:
        data = {}

    return OutlineResponse(
        title=str(data.get("title", fallback_title)),
        hook=str(data.get("hook", "")),
        description=str(data.get("description", "")),
        sections=[str(section) for section in data.get("sections", [])],
        examples=[str(example) for example in data.get("examples", [])],
        cta=str(data.get("cta", "")),
    )


def _build_fallback_outline(topic: str) -> OutlineResponse:
    title = topic.strip() or "Untitled video"
    return OutlineResponse(
        title=title,
        hook=f"Why {title} matters right now",
        description=(
            f"A quick starter outline for {title} that you can refine further."
        ),
        sections=[
            "Introduce the topic and its relevance",
            "Share 3 key points or lessons",
            "Add a practical example or case study",
            "End with a clear takeaway and CTA",
        ],
        examples=[
            f"Show a real example related to {title}",
            f"Compare {title} with a common alternative",
        ],
        cta=f"Subscribe for more ideas about {title}",
    )


def generate_outline(request: TopicRequest) -> OutlineResponse:
    try:
        raw_outline = generate_outline_text(request.title)
    except Exception:
        return _build_fallback_outline(request.title)

    if isinstance(raw_outline, str):
        try:
            payload = json.loads(raw_outline)
        except json.JSONDecodeError:
            payload = {
                "title": request.title,
                "hook": "",
                "description": raw_outline,
                "sections": [],
                "examples": [],
                "cta": "",
            }
    else:
        payload = raw_outline

    return _coerce_outline(payload, request.title)
