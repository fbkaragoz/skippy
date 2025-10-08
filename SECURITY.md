# Security Guidelines

## API Key Management

### ⚠️ IMPORTANT: Never Commit API Keys

This repository previously contained exposed API keys. All hardcoded keys have been removed and invalidated.

### How to Securely Store API Keys

1. **Use Environment Variables**
   - Copy `.env.example` to `.env`
   - Fill in your actual API keys in `.env`
   - The `.env` file is gitignored and won't be committed

2. **Load Environment Variables in Your Code**

   ```python
   import os
   from dotenv import load_dotenv
   
   # Load environment variables from .env file
   load_dotenv()
   
   # Access API keys
   gpt_api_key = os.getenv('GPT_API_KEY')
   youtube_api_key = os.getenv('YOUTUBE_API_KEY')
   discord_token = os.getenv('DISCORD_TOKEN')
   ```

3. **Never Commit Sensitive Files**
   - API keys
   - Tokens
   - Private keys
   - Credentials
   - `.env` files

### Files to Keep Secure

The following files should NEVER contain real API keys:
- `api/info/tokens.txt` - Now contains only comments
- `gpt.py` - Now uses environment variables
- Any files in `secret/` directory

### What to Do If You Expose an API Key

1. **Immediately revoke/regenerate** the exposed key from the service provider
2. **Remove the key** from all commits in git history
3. **Update** all services using the old key
4. **Never reuse** an exposed key

### Recommended Tools

- **python-dotenv**: Load environment variables from `.env` files
- **git-secrets**: Prevent committing secrets to git
- **truffleHog**: Scan git history for secrets

## Reporting Security Issues

If you discover a security vulnerability, please email the maintainer directly rather than opening a public issue.
