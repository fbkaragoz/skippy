import time
import json

class BotHandler:
    def __init__(self, recent_file):

        self.recent_file = recent_file
        self.context = []

    def add_dialogue(self, dialogue):
        if len(self.context) == 15:
            self.context.pop(0)

        self.context.append(dialogue)

        if self.has_recurring_phrases(dialogue):
            self.save_important_dialogue(dialogue)

    def has_recurring_phrases(self, dialogue):
        words = set(dialogue.split())
        for sentence in self.context[:-1]:
            if words & set(sentence.split()):
                return True
        return False

    def save_important_dialogue(self, dialogue):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        data = {"timestamp": timestamp, "dialogue": dialogue}

        with open(self.recent_file, 'a', encoding='utf-8') as file:
            file.write(json.dumps(data) + '\n')

    def get_context(self):
        return self.context


bot_handler = BotHandler('recent_data/recent_dialogues.txt')
bot_handler.add_dialogue()
bot_handler.has_recurring_phrases()
bot_handler.save_important_dialogue()

