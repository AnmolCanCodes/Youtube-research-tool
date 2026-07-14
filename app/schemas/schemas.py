from pydantic import BaseModel, ConfigDict


class TopicRequest(BaseModel):
    title: str


class OutlineResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    title: str
    hook: str
    description: str
    sections: list[str]
    examples: list[str]
    cta: str