# Security Remediation Checklist

## ✅ Completed by This PR

- [x] Identified all exposed API keys in the repository
- [x] Removed hardcoded API keys from all source files
- [x] Created `.gitignore` to prevent future exposure
- [x] Created `.env.example` template for configuration
- [x] Added comprehensive `SECURITY.md` documentation
- [x] Updated all Python code to use environment variables
- [x] Added security warnings to legacy/insecure code
- [x] Created `requirements.txt` with security dependencies
- [x] Updated README with security notice and setup instructions

## ⚠️ ACTION REQUIRED: Repository Owner Tasks

### IMMEDIATE (Do Today)

- [ ] **Revoke OpenAI API Key**: 
  - Go to https://platform.openai.com/api-keys
  - Revoke key starting with `4u3wGFOVuvEGS...`
  - Generate new key
  - Update in production environment

- [ ] **Revoke YouTube API Key**:
  - Go to https://console.cloud.google.com/apis/credentials
  - Revoke key `AIzaSyBDM7xg0...`
  - Create new credentials
  - Update in production environment

- [ ] **Revoke Discord Bot Token**:
  - Go to https://discord.com/developers/applications
  - Navigate to your application
  - Regenerate bot token (under Bot section)
  - Update in production environment

- [ ] **Check for unauthorized usage**:
  - Review OpenAI usage dashboard for suspicious activity
  - Check Google Cloud Console for YouTube API calls
  - Review Discord application logs

### HIGH PRIORITY (This Week)

- [ ] **Set up local development environment**:
  ```bash
  cd /path/to/skippy
  cp .env.example .env
  # Edit .env with your NEW API keys
  pip install -r requirements.txt
  ```

- [ ] **Update deployment/CI environments**:
  - Add `GPT_API_KEY` environment variable
  - Add `YOUTUBE_API_KEY` environment variable
  - Add `DISCORD_TOKEN` environment variable
  - Ensure `.env` files are NOT in version control

- [ ] **Test the application**:
  - Run discord bot: `python run/discord/discord.py`
  - Verify all API integrations work with new keys
  - Check error logs for missing environment variables

### RECOMMENDED (This Month)

- [ ] **Clean git history** (removes keys from old commits):
  ```bash
  # Install BFG Repo-Cleaner
  # macOS: brew install bfg
  # Linux: download from https://rtyley.github.io/bfg-repo-cleaner/
  
  # Create list of exposed secrets
  cat > passwords.txt << EOF
  4u3wGFOVuvEGSQPpfsmJT3BlbkFJWrUHSPh7ICEXhQsfnPuB
  AIzaSyBDM7xg03Ch6KY0V5lxpgPc9PpGnhYgVCI
  MTE5MDA0Mzg4ODcyMzk3MjE2Ng.GQMqi_.-EyBVvcQySoUU-85l42ST__AJImryl2fGLRdNc
  EOF
  
  # Run BFG to remove secrets from history
  bfg --replace-text passwords.txt
  
  # Clean up git references
  git reflog expire --expire=now --all
  git gc --prune=now --aggressive
  
  # Force push (WARNING: coordinate with team first!)
  git push --force --all
  
  # Clean up
  rm passwords.txt
  ```

- [ ] **Set up secret scanning**:
  - Enable GitHub Secret Scanning (if available)
  - Or use third-party tools like GitGuardian
  - Configure alerts for exposed secrets

- [ ] **Add pre-commit hooks**:
  ```bash
  # Install git-secrets
  brew install git-secrets  # macOS
  # or download from https://github.com/awslabs/git-secrets
  
  # Set up hooks
  cd /path/to/skippy
  git secrets --install
  git secrets --register-aws
  git secrets --add 'sk-[a-zA-Z0-9]{32,}'  # OpenAI pattern
  git secrets --add 'AIza[a-zA-Z0-9_-]{35}'  # Google API pattern
  ```

- [ ] **Review access controls**:
  - Audit who has access to API keys
  - Implement principle of least privilege
  - Use service accounts where possible
  - Enable API key restrictions (IP whitelisting, domain restrictions)

- [ ] **Set up proper secret management**:
  - Consider AWS Secrets Manager, HashiCorp Vault, or similar
  - Implement key rotation policies
  - Use different keys for dev/staging/production

### ONGOING

- [ ] **Regular security audits**:
  - Review repository for sensitive data monthly
  - Check for new team members' commits
  - Audit API usage regularly

- [ ] **Team education**:
  - Share `SECURITY.md` with all contributors
  - Require code reviews for all changes
  - Train team on secure coding practices

- [ ] **Monitor for breaches**:
  - Set up alerts for unusual API usage
  - Monitor service dashboards regularly
  - Subscribe to security advisories

## 📚 Resources

- **SECURITY.md** - Comprehensive security guidelines
- **.env.example** - Environment variable template
- **requirements.txt** - Dependencies including python-dotenv
- **GitHub Secret Scanning** - https://docs.github.com/en/code-security/secret-scanning
- **BFG Repo-Cleaner** - https://rtyley.github.io/bfg-repo-cleaner/
- **git-secrets** - https://github.com/awslabs/git-secrets

## 🆘 Need Help?

If you have questions about:
- How to regenerate specific API keys → Check service provider documentation
- How to clean git history → See "Clean git history" section above
- How to set up environment variables → See `.env.example` and `SECURITY.md`
- Security best practices → See `SECURITY.md`

## 📊 Summary

**Exposed Keys**: 3 (OpenAI, YouTube, Discord)
**Files Modified**: 12
**New Security Files**: 5
**Risk Level Before**: 🔴 CRITICAL
**Risk Level After**: 🟡 MEDIUM (after owner regenerates keys)
**Risk Level Target**: 🟢 LOW (after git history cleaned)
