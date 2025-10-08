import logging
from typing import Optional

import discord
from discord.ext import commands

from config import Config
from .handlers import MessageHandler


class SkippyBot(commands.Bot):
    """Discord bot wrapper that wires configuration and shared services."""

    def __init__(
        self,
        *,
        config: Config,
        message_handler: MessageHandler,
        command_prefix: str = "!",
        intents: Optional[discord.Intents] = None,
    ) -> None:
        self.config = config
        self.message_handler = message_handler
        self.log = logging.getLogger(__name__)

        computed_intents = intents or self._build_default_intents()
        super().__init__(command_prefix=command_prefix, intents=computed_intents)
        self.log.debug("SkippyBot instantiated with prefix %s", command_prefix)

    @staticmethod
    def _build_default_intents() -> discord.Intents:
        """Enable the intents we need while keeping others disabled."""
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        intents.reactions = True
        return intents

    async def on_ready(self) -> None:
        """Log connection details once Discord authorises the bot."""
        self.log.info("Connected as %s (id=%s)", self.user, getattr(self.user, "id", "?"))

    async def on_message(self, message: discord.Message) -> None:
        """Delegate message handling then keep default command processing."""
        await self.message_handler.handle(message=message, bot=self)
        await super().on_message(message)
