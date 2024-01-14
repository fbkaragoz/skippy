import re


API_TOKENS = '/Users/felixfelicis/PycharmProjects/DiscordBot/api/tokens.txt'#log infrentials

def get_api_keys(*token_all):
    api_keys = {}
    with open(API_TOKENS, 'r', encoding='utf-8') as f:
        for line in f:
            match = re.match(r'(\w+)\s*=\s*(.+)', line.strip())
            if match:
                key, value = match.groups()
                api_keys[key] = value

    return api_keys

def add_api_keys(*token_all):
    pass


api_locker = get_api_keys()


"""for key, value in api_locker.items():
    print(key + ':', value.strip())"""
