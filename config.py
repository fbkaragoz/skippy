import os
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError as exc:
    raise ImportError(
        "Missing dependency 'python-dotenv'. Install via `pip install python-dotenv`."
    ) from exc


class Config:
    PROJECT_ROOT = Path(__file__).resolve().parent
    ENV_FILE = PROJECT_ROOT / ".env"

    """DIRECTORIES"""
    DATA_DIR = PROJECT_ROOT / "data"  # TODO: implement data handling
    LOGS_DIR = PROJECT_ROOT / "logs"  # TODO: implement logging
    TEMP_DIR = PROJECT_ROOT / "temp"  # TODO: implement temp file handling
    PROMPTS_DIR = PROJECT_ROOT / "prompts"
    # MODEL_DIR = PROJECT_ROOT / "models" #NOTE: decide if any local models are needed in future
    SYSTEM_PROMPT_FILE = PROMPTS_DIR / "system.txt"

    load_dotenv(ENV_FILE, verbose=True)  # load environment variables

    ENVIRONMENT = os.getenv(
        "ENVIRONMENT", "development"
    )  # TODO: implement environment handling for dev

    """API KEYS LOADED FROM .ENV"""
    DC_TOKEN = os.getenv("DC_TOKEN")  # discord token
    OAI_TOKEN = os.getenv("OAI_TOKEN")  # openai token
    X_TOKEN = os.getenv("X_TOKEN")  # twitter/x token

    """MODEL & BOT SETTINGS"""
    OAI_MODEL = os.getenv("OAI_MODEL")
    BOT_SYSTEM_PROMPT_ENV = os.getenv("BOT_SYSTEM_PROMPT")
    BOT_SYSTEM_PROMPT_PATH = os.getenv("BOT_SYSTEM_PROMPT_PATH")
    BOT_REPLY_MODE = os.getenv("BOT_REPLY_MODE", "mention_or_dm")

    @classmethod
    def ensure_dirs(cls):
        cls.DATA_DIR.mkdir(parents=True, exist_ok=True)
        cls.LOGS_DIR.mkdir(parents=True, exist_ok=True)
        cls.TEMP_DIR.mkdir(parents=True, exist_ok=True)
        cls.PROMPTS_DIR.mkdir(parents=True, exist_ok=True)
        # cls.MODEL_DIR.mkdir(parents=True, exist_ok=True)

    @classmethod
    def validate(cls):
        valid_envs = {"development", "staging", "production"}
        assert (
            cls.ENVIRONMENT in valid_envs
        ), f"INVALID ENVIRONMENT! USE ONE OF: {valid_envs}"
        assert cls.DC_TOKEN, "Missing DC_TOKEN"
        assert cls.OAI_TOKEN, "Missing OAI_TOKEN"
        assert cls.OAI_MODEL, "Missing OAI_MODEL"
        assert cls.get_system_prompt().strip(), "System prompt cannot be empty"

    @classmethod
    def as_dict(cls):
        return {
            "environment": cls.ENVIRONMENT,
            "project_root": cls.PROJECT_ROOT,
            "directories": {
                "data": cls.DATA_DIR,
                "logs": cls.LOGS_DIR,
                "temp": cls.TEMP_DIR,
                # 'models': cls.MODEL_DIR,
            },
            "tokens": {
                "discord": cls.DC_TOKEN,
                "openai": cls.OAI_TOKEN,
                "x": cls.X_TOKEN,
            },
            "openai": {"model": cls.OAI_MODEL},
            "bot": {
                "reply_mode": cls.BOT_REPLY_MODE,
                "system_prompt_path": cls.BOT_SYSTEM_PROMPT_PATH,
            },
        }

    @classmethod
    def get_system_prompt(cls) -> str:
        """Fetch the system prompt from env or configured file."""
        if cls.BOT_SYSTEM_PROMPT_ENV:
            return cls.BOT_SYSTEM_PROMPT_ENV.strip()

        prompt_path = (
            Path(cls.BOT_SYSTEM_PROMPT_PATH).expanduser()
            if cls.BOT_SYSTEM_PROMPT_PATH
            else cls.SYSTEM_PROMPT_FILE
        )

        if prompt_path.exists():
            return prompt_path.read_text(encoding="utf-8").strip()

        raise FileNotFoundError(
            "No system prompt found. Set BOT_SYSTEM_PROMPT or create prompts/system.txt."
        )


if __name__ == "__main__":
    Config.ensure_dirs()
    Config.validate()
