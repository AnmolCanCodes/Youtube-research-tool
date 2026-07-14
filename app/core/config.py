from pathlib import Path

from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    OPENAI_API_KEY: str | None = None
    GEMINI_API_KEY: str | None = None
    MODEL_NAME: str = "gpt-4.1-mini"

    class Config:
        env_file = Path(__file__).resolve().parents[2] / ".env"
        extra = "ignore"


settings = Settings()