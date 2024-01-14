import re
import os

API_TOKENS = '.tokens.bin'
directory_root = './info'

tokens_file_path = os.path.join(directory_root, API_TOKENS)

def get_api_keys(*tokens):


    api_keys = {}

    with open(tokens_file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

        for line in lines:
            match = re.match(r'(\w+)\s*=\s*(.+)', line)

            if match:
                key, value = match.groups()
                api_keys[key] = value


        return api_keys


api_locker = get_api_keys()



for k, v in api_locker.items():
    print(k, v)