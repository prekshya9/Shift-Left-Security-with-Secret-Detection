"""
This file contains intentionally exposed secrets for educational purposes.
Your task is to find and fix these security issues using Gitleaks.

CHALLENGE: Find and fix all the secrets in this file!
"""

# AWS Credentials (Format: AKIA + 16 characters)
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# Database Credentials
DB_PASSWORD = "super_secret_db_password_123"
DB_CONNECTION = "postgresql://user:password123@localhost:5432/mydb"

# API Keys
STRIPE_API_KEY = "sk_test_51HxEXAMPLE"
GITHUB_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwxyz"

# JWT Secret
JWT_SECRET = "my-super-secret-jwt-key-that-should-not-be-here"

# SSH Private Key (partial example)
SSH_PRIVATE_KEY = """
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA1c7+9z5Pad7OejecsQ0buoLoWQBXz6XhCr9c5Y0Bk0w
-----END RSA PRIVATE KEY-----
"""

def main():
    """
    This function demonstrates how NOT to handle secrets in code.
    In a real application, these should be stored in environment variables
    or a secure secrets management system.
    """
    print("This is a challenge file!")
    print("Try to find all the secrets using Gitleaks!")
    print("Then fix them by moving them to environment variables.")

if __name__ == "__main__":
    main() 