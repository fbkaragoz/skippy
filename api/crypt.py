"""
SECURITY WARNING: This module is deprecated due to insecure key handling.

Issues:
- Base64 encoding is NOT encryption (it's easily reversible)
- Loading keys from files is insecure
- Printing encoded keys exposes them

Recommended approach:
- Use environment variables for API keys
- Use proper encryption libraries (cryptography, PyNaCl) if encryption is needed
- Never print or log API keys
"""

import base64
import os

class Cryption:
    def __init__(self):
        self.crypted_value = ""

    def recall_values(self):
        """
        DEPRECATED: Use environment variables instead.
        
        Example:
            api_keys = {
                'gpt': os.getenv('GPT_API_KEY'),
                'youtube': os.getenv('YOUTUBE_API_KEY'),
                'discord': os.getenv('DISCORD_TOKEN')
            }
        """
        # Do not load from token_manager to avoid exposing keys
        print("Warning: This method is deprecated. Use environment variables.")
        return self.crypted_value

    def encode_values(self):
        """
        WARNING: Base64 is NOT encryption!
        If you need encryption, use proper cryptography libraries.
        """
        if self.crypted_value:
            bytes_value = self.crypted_value.encode("ascii")
            base64_bytes = base64.b64encode(bytes_value)
            # Don't print encoded values
            print("Warning: Encoding is not secure. Use proper encryption.")


# Do not auto-execute - prevents accidental key exposure
if __name__ == '__main__':
    print("This module is deprecated. Please use environment variables for API keys.")
    print("See SECURITY.md for proper API key management.")


