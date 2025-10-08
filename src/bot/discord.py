from discord.ext import commands
import discord
import handler
import random
import os
token_path = '../../api'



class DiscordBot(commands.Bot):
    def __init__(self, command_prefix, *args, **kwargs):
        intents = discord.Intents.default()
        all_intents = ['reactions', 'messages', 'members', 'presences']
        intents_defined = [all_intents for _ in all_intents]
        intents.intents_defined = True

        super().__init__(command_prefix, intents=intents, *args, **kwargs)
        self.token = os.getenv('DISCORD_TOKEN')
        self.gpt_api_key = GPT_API_KEY
        self.youtube_api_key = YOUTUBE_API_KEY
        self.token = DISCORD_TOKEN
        self.bot_handler = handler.BotHandler('../../recent_data/recent_dialogues.txt')
        self.interest_keywords = ['alice', 'ai', 'cdli', 'fun', 'music']

    async def on_message(self, message):
        if message.author == self.user:
            return

        self.bot_handler.add_dialogue(message.content)

        if self.is_message_interesting(message.content):
            response = self.generate_gpt_response(message.content)
            await message.channel.send(response)

        if 'music' in message.content.lower():
            music_link = self.recommend_music()
            await message.channel.send(music_link)

    def is_message_interesting(self, message_content):
        return any(keyword in message_content.lower() for keyword in self.interest_keywords)

    def generate_gpt_response(self, message_content):
        prompt = self.create_custom_prompt(message_content)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Alice, an assistant AI."},
                {"role": "user", "content": message_content},
            ]
        )
        return response.choices[0].message['content']

    def recommend_music(self):
        genres = ['minimal techno', 'rock']
        chosen_genre = random.choice(genres)
        music_link = self.fetch_youtube_link(chosen_genre)
        return music_link

    def fetch_youtube_link(self, genre):
        youtube = build('youtube', 'v3', developerKey=self.youtube_api_key)
        request = youtube.search().list(q=genre, part='snippet', type='video', maxResults=1)
        response = request.execute()

        if response['items']:
            video_id = response['items'][0]['id']['videoId']
            return f"https://www.youtube.com/watch?v={video_id}"
        else:
            return "No music found."

    def create_custom_prompt(self, message_content):
        self_intro = "I am Alice, an assistant AI. "
        contextual_knowledge = self.get_contextual_knowledge()
        prompt = f"{self_intro} {contextual_knowledge} How should I respond to: '{message_content}'?"
        return prompt


    def get_contextual_knowledge(self):

        try:
            with open('contextual_knowledge.txt', 'r') as file:
                knowledge = file.read()
            return knowledge
        except FileNotFoundError:
            return ("I'm 25 years old, living in two realities,"
                    " aiming to achieve Singularity.")

    def run(self):
        super().run(self.token)


bot = DiscordBot(command_prefix='-')
bot.run()




