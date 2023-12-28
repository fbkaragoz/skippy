from discord.ext import commands
import openai
import handler

class DiscordBot(commands.Bot):
    def __init__(self, token, gpt_api_key, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.token = token
        self.gpt_api_key = gpt_api_key
        self.bot_handler = handler.BotHandler('../recent_data/recent_dialogues.txt')

    async def on_message(self, message):
        if message.author == self.user:
            return
