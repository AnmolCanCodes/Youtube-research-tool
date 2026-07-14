import httpx
from openai import OpenAI

try:
    from app.core.config import settings
    from app.llms.prompt import SYSTEM_PROMPT, USER_PROMPT
except ModuleNotFoundError:  
    from core.config import settings
    from llms.prompt import SYSTEM_PROMPT, USER_PROMPT


def _build_messages(topic: str) -> list[dict[str, str]]:
    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": USER_PROMPT.format(topic=topic)},
    ]


def generate_outline_text(topic: str) -> str:
    if settings.OPENAI_API_KEY:
        client = OpenAI(api_key=settings.OPENAI_API_KEY)
        response = client.chat.completions.create(
            model=settings.MODEL_NAME or "gpt-4.1-mini",
            messages=_build_messages(topic),
            temperature=0.3,
        )
        return response.choices[0].message.content or ""

    if settings.GEMINI_API_KEY:
        model_name = settings.MODEL_NAME or "gemini-2.0-flash"
        url = (
            f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent"
            f"?key={settings.GEMINI_API_KEY}"
        )
        payload = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": (
                                f"{SYSTEM_PROMPT}\n\n"
                                f"{USER_PROMPT.format(topic=topic)}"
                            )
                        }
                    ]
                }
            ],
            "generationConfig": {"temperature": 0.3},
        }
        response = httpx.post(url, json=payload, timeout=60.0)
        response.raise_for_status()
        data = response.json()
        return data["candidates"][0]["content"]["parts"][0]["text"]

    raise RuntimeError("No API key configured for the LLM client.")