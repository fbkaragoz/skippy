import logging
from typing import Mapping, Sequence

from openai import AsyncOpenAI


Message = Mapping[str, str]


class OpenAIChatService:
    """Async wrapper around the OpenAI chat completion endpoint."""

    def __init__(self, *, api_key: str, model: str) -> None:
        self._client = AsyncOpenAI(api_key=api_key)
        self._model = model
        self._log = logging.getLogger(__name__)

    async def complete(self, messages: Sequence[Message]) -> str:
        """Send a chat completion request and return the assistant reply."""
        try:
            response = await self._client.chat.completions.create(
                model=self._model,
                messages=list(messages),
            )
        except Exception as exc:  # broad catch to surface errors upstream
            self._log.exception("OpenAI chat call failed: %s", exc)
            raise

        choice = response.choices[0]
        content = choice.message.content or ""
        if not content:
            self._log.warning("OpenAI returned empty content.")
        return content.strip()
