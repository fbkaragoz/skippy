import sys
sys.path.append('../api')
import token_manager
api_keys = token_manager.get_api_keys()

for k,v in api_keys.items():
    print(f"Server: {k}, Token: {v}")

