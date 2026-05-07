# Secret Detection Lab

This is a hands-on lab to practice detecting secrets in code using Gitleaks. Learn how to implement Shift-Left Security practices by finding and fixing exposed secrets early in the development cycle.

## Prerequisites

- Git
- Python 3.8+
- Gitleaks (installation instructions below)

## Setup

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd secret-detection-lab
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Install Gitleaks:
   - macOS: `brew install gitleaks`
   - Linux: `snap install gitleaks`
   - Windows: Download from [Gitleaks releases](https://github.com/zricethezav/gitleaks/releases)

4. (Optional) Install pre-commit hooks:
   ```bash
   pip install pre-commit
   pre-commit install
   ```

## Lab Exercise

### Basic Exercise
1. **Initial Scan**
   - Run Gitleaks to detect secrets:
     ```bash
     gitleaks detect --source .
     ```
   - You should see a detection of the AWS secret in the `.env` file

2. **Fix the Issue**
   - Remove the secret from the `.env` file
   - Run Gitleaks again to verify the fix:
     ```bash
     gitleaks detect --source .
     ```
   - The scan should now be clean

### Advanced Challenge
1. **Secret Hunt**
   - Open `secrets_challenge.py`
   - Use Gitleaks to find all the secrets in this file
   - Fix each secret by:
     - Moving it to the `.env` file
     - Updating the code to use environment variables
     - Running Gitleaks again to verify your fixes

2. **Pre-commit Protection**
   - Try to commit a file with a secret
   - The pre-commit hook should prevent the commit
   - Fix the secret and try again

## Learning Objectives

- Understand how secrets can be accidentally exposed in code
- Learn to use Gitleaks for secret detection
- Practice implementing Shift-Left Security
- Understand the importance of proper secret management
- Learn to use pre-commit hooks for security
- Understand CI/CD security scanning

## Best Practices

- Never commit real secrets to version control
- Use `.gitignore` to prevent sensitive files from being committed
- Consider using a secrets management service in production
- Implement pre-commit hooks with Gitleaks in real projects
- Use environment variables for configuration
- Regular security scanning in CI/CD pipelines

## Real-World Examples

This lab includes examples of common secret types:
- AWS credentials
- Database connection strings
- API keys
- JWT secrets
- SSH private keys

## Additional Resources

- [Gitleaks Documentation](https://github.com/zricethezav/gitleaks)
- [AWS Security Best Practices](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html)
- [OWASP Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
- [Pre-commit Documentation](https://pre-commit.com/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- ## Reflection
- What kinds of secrets were detected?
During this lab i have seen the key of various code such as AWS keys,Datbase cendential,API keys ,SSh etc where their secerts are unlocked and can be accessible to everyone 

How would this affect a production app?
This may give access to the hacker where they can have access to the main system where they can misplace the password hack the entire system and do whatever they wanted to do 

What tools or habits will help you avoid leaking secrets in the future?
By masking the py file or by not leaving the real passowrd there,by using.env file to keep the data secrete and by using gitleaks command precommit hook which help to  avoid risk to the system by denying the deployment without keeping it safe  