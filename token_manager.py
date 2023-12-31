import re

API_TOKENS = 'tokens.txt'

def get_api_keys():
    api_keys = {
        'gpt_api_key': None,
        'youtube_api_key': None,
        'discord_api_key': None,
        'twitter_api_key': None
    }

    with open(API_TOKENS, 'r', encoding='utf-8') as f:
        token_lines = f.readlines()
        for line in token_lines:
            match = re.match(r'(\w+)\s*=\s*(.+)', line)

            if match:
                key, value = match.groups()
                api_keys[key] = value



        return api_keys

