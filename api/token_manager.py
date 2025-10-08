import re
import os

API_TOKENS = '.tokens.bin'
directory_root = './info'

tokens_file_path = os.path.join(directory_root, API_TOKENS)

def get_api_keys(*tokens):
    """
    Load API keys from a secure token file.
    
    SECURITY WARNING: Tokens should be encrypted or loaded from environment variables.
    This function is for backward compatibility only.
    
    Recommended: Use environment variables instead:
        import os
        api_key = os.getenv('API_KEY_NAME')
    """
    api_keys = {}
    
    if not os.path.exists(tokens_file_path):
        print(f"Warning: Token file not found at {tokens_file_path}")
        print("Please use environment variables for API keys.")
        return api_keys

    try:
        with open(tokens_file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

            for line in lines:
                # Skip comments and empty lines
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                    
                match = re.match(r'(\w+)\s*=\s*(.+)', line)

                if match:
                    key, value = match.groups()
                    api_keys[key] = value.strip()

    except Exception as e:
        print(f"Error reading token file: {e}")
        
    return api_keys


# Only load keys if running directly (not imported)
if __name__ == '__main__':
    api_locker = get_api_keys()
    
    if api_locker:
        for k, v in api_locker.items():
            print(f"{k}: {'*' * len(v)}")  # Don't print actual values
    else:
        print("No API keys loaded. Please configure environment variables.")