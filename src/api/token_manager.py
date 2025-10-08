import os
from dotenv import load_dotenv

class TokenManager:
    def __init__(self):
        load_dotenv()

    def get_dc_token(self):
        try:
            return os.getenv('DISCORD_TOKEN')
        except Exception as e:
            raise ValueError("Failed to retrieve Discord token") from e

    def get_oai_token(self):
        try:
            return os.getenv('OPENAI_TOKEN')
        except Exception as e:
            raise ValueError("Failed to retrieve OpenAI token") from e

    def get_x_token(self):
        try:
            return os.getenv('X_TOKEN')
        except Exception as e:
            raise ValueError("Failed to retrieve X token") from e
        
        
