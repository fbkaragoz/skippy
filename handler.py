import json
import time
from collections import deque
from typing import List

class BotHandler:
    def __init__(self, recent_file: str, context_length: int = 15):
        """
        Initializes the bot handler with a file to save important dialogues and a context length.
        """
        self.recent_file = recent_file
        self.context = deque(maxlen=context_length)



    def add_dialogue(self, dialogue: str):
        """
        Adds a dialogue to the context and saves it if it contains recurring phrases.
        """
        self.context.append(dialogue)
        if self.has_recurring_phrases(dialogue):
            self.save_important_dialogue(dialogue)

    def has_recurring_phrases(self, dialogue: str) -> bool:
        """
        Checks if the dialogue has words that recur in the context.
        """
        words = set(dialogue.split())
        for sentence in self.context:
            if words & set(sentence.split()):
                return True
        return False

    def save_important_dialogue(self, dialogue: str):
        """
        Saves an important dialogue to the file.
        """
        try:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            data = {"timestamp": timestamp, "dialogue": dialogue}
            with open(self.recent_file, 'a', encoding='utf-8') as file:
                file.write(json.dumps(data) + '\n')
        except IOError as e:
            print(f"An error occurred while writing to the file: {e}")

    def get_context(self) -> List[str]:
        """
        Returns the current context as a list.
        """
        return list(self.context)
