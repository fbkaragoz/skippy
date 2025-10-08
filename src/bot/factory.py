import logging

from config import Config
from src.services.openai_client import OpenAIChatService

from .discord import SkippyBot
from .handlers import MessageHandler


def create_bot(*, config: Config, command_prefix: str = "!") -> SkippyBot:
    """Factory to build a configured Discord bot instance."""
    config.ensure_dirs()
    config.validate()

    openai_service = OpenAIChatService(
        api_key=config.OAI_TOKEN,
        model=config.OAI_MODEL,
    )
    message_handler = MessageHandler(config=config, openai_service=openai_service)

    bot = SkippyBot(
        config=config,
        message_handler=message_handler,
        command_prefix=command_prefix,
    )
    logging.getLogger(__name__).debug("Created SkippyBot via factory.")
    return bot
