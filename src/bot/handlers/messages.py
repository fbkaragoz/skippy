from dataclasses import dataclass
from typing import Sequence

import discord

from config import Config
from src.services.openai_client import OpenAIChatService


@dataclass
class MessageHandler:
    """Route Discord messages to OpenAI while obeying config rules."""

    config: Config
    openai_service: OpenAIChatService

    async def handle(self, *, message: discord.Message, bot: discord.Client) -> None:
        if message.author.bot:
            return

        if not self._should_reply(message, bot):
            return

        prompt_messages = self._build_prompt(message)
        try:
            reply_text = await self.openai_service.complete(prompt_messages)
        except Exception:
            # Failure already logged inside the service.
            return

        if reply_text:
            await message.channel.send(reply_text)

    def _build_prompt(self, message: discord.Message) -> Sequence[dict]:
        system_content = self.config.get_system_prompt()
        user_message = message.content.strip()
        return [
            {"role": "system", "content": system_content},
            {"role": "user", "content": user_message or "Respond to an empty message."},
        ]

    def _should_reply(self, message: discord.Message, bot: discord.Client) -> bool:
        mode = (self.config.BOT_REPLY_MODE or "mention_or_dm").lower()

        if mode == "all":
            return True

        is_dm = message.guild is None
        if mode == "dm":
            return is_dm

        if mode == "mention_or_dm":
            mentioned = bool(bot.user and bot.user in message.mentions)
            return is_dm or mentioned

        # Default: only react to direct mentions.
        return bool(bot.user and bot.user in message.mentions)
