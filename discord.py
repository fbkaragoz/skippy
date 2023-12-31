from discord.ext import commands
import discord
import token_manager
from gpt import response
from bot_handler import BotHandler  # Import the BotHandler class


class ConnAPI(commands.Bot):
    def __init__(self, command_prefix, *args, **kwargs):
        # ... [rest of your bot initialization code]

        api_keys = token_manager.get_api_keys()
        self.gpt_api_key = api_keys['gpt_api_key']

        self.bot_handler = BotHandler('recent_dialogues.txt')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('!talk'):
            self.bot_handler.add_dialogue(message.content)
            context = self.bot_handler.get_context()

            prompt = message.content[len('!talk '):]
            response = gpt_response(prompt, context, self.gpt_api_key)

            if response:
                await message.channel.send(response)
                self.bot_handler.add_dialogue(response)

        intents = discord.Intents.default()
        intents.messages = True
        intents.reactions = True
        intents.members = True
        intents.presences = True

        super().__init__(command_prefix, intents=intents, *args, **kwargs)

        api_keys = token_manager.get_api_keys()
        self.gpt_api_key = api_keys['gpt_api_key']
        self.youtube_api_key = api_keys['youtube_api_key']
        self.discord_api_key = api_keys['discord_api_key']
        self.twitter_api_key = api_keys['twitter_api_key']


bot = ConnAPI(command_prefix='!')
if bot.discord_api_key:
    bot.run(bot.discord_api_key)
else:
    print("Discord API key is missing.")
