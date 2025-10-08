from pathlib import Path
import os
from dotenv import load_dotenv


class Config:
    PROJECT_ROOT = Path(__file__).resolve.parent
    ENV_FILE = PROJECT_ROOT / ".env"

    """DIRECTORIES"""
    DATA_DIR = PROJECT_ROOT / "data" #TODO: implement data handling
    LOGS_DIR = PROJECT_ROOT / "logs" #TODO: implement logging
    TEMP_DIR = PROJECT_ROOT / "temp" #TODO: implement temp file handling
    # MODEL_DIR = PROJECT_ROOT / "models" #NOTE: decide if any local models are needed in future

    load_dotenv(ENV_FILE, verbose=True) # load environment variables

    ENVIRONMENT = os.getenv("ENVIRONMENT", "development") #TODO: implement environment handling for dev

    """API KEYS LOADED FROM .ENV"""
    DC_TOKEN = os.getenv("DC_TOKEN") # discord token
    OAI_TOKEN = os.getenv("OAI_TOKEN") # openai token
    X_TOKEN = os.getenv("X_TOKEN") # twitter/x token

    @classmethod
    def ensure_dirs(cls):
        cls.DATA_DIR.mkdir(parents=True, exist_ok=True)
        cls.LOGS_DIR.mkdir(parents=True, exist_ok=True)
        cls.TEMP_DIR.mkdir(parents=True, exist_ok=True)
        # cls.MODEL_DIR.mkdir(parents=True, exist_ok=True)

    @classmethod
    def validate(cls):
        valid_envs = {"development", "staging", "production"}
        assert cls.ENVIRONMENT in valid_envs, f"INVALID ENVIRONMENT! USE ONE OF: {valid_envs}"
        assert cls.DC_TOKEN, "Missing DC_TOKEN"
        assert cls.OAI_TOKEN, "Missing OAI_TOKEN"
        assert cls.X_TOKEN, "Missing X_TOKEN"

Config.ensure_dirs()
Config.validate()
