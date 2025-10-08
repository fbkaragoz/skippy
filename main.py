import logging
from config import Config
from src.bot.factory import create_bot


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    bot = create_bot(config=Config, command_prefix="!")
    bot.run(Config.DC_TOKEN)


if __name__ == "__main__":
    main()
