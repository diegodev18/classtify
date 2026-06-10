from typing import Any

import httpx

from app.config import settings


class OpenRouterError(Exception):
    pass


class OpenRouterClient:
    def __init__(
        self,
        api_key: str | None = None,
        base_url: str | None = None,
        default_model: str | None = None,
    ) -> None:
        self.api_key = api_key or settings.openrouter_api_key
        self.base_url = base_url or settings.openrouter_base_url
        self.default_model = default_model or settings.openrouter_default_model

    def _headers(self) -> dict[str, str]:
        if not self.api_key:
            raise OpenRouterError(
                "OPENROUTER_API_KEY is not configured. Set it in your environment."
            )
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    async def chat(
        self,
        messages: list[dict[str, str]],
        *,
        model: str | None = None,
    ) -> dict[str, Any]:
        payload = {
            "model": model or self.default_model,
            "messages": messages,
        }

        async with httpx.AsyncClient(base_url=self.base_url, timeout=60.0) as client:
            response = await client.post("/chat/completions", json=payload, headers=self._headers())

        if response.status_code >= 400:
            raise OpenRouterError(f"OpenRouter request failed: {response.text}")

        return response.json()
