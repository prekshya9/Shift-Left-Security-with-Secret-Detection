"""
This file contains intentionally exposed secrets for educational purposes.
Your task is to find and fix these security issues using Gitleaks.

CHALLENGE: Find and fix all the secrets in this file!
"""

# AWS Credentials (Format: AKIA + 16 characters)
#This is the key password for the cloud keeping it here can give acess to anyone and have control over our servers
AWS_ACCESS_KEY = "MASKED_ACCESS_KEY"
AWS_SECRET_KEY = "MASKED_SECRET_KEY"

# Database Credentials
# It has login information of database its risky cause anyone can have this access which can cause  information lekage
DB_PASSWORD = "MASKED_PASSWORD"
DB_CONNECTION = "postgresql://user:MASKED_PASSWORD@localhost:5432/mydb"

# API Keys
#It is the code talk between two parties it is risky cause someone can interfere between the connection like man in the middle 
STRIPE_API_KEY = "REPLACED_BY_CONFIG"
GITHUB_TOKEN = "MASKED_GITHUB_TOKEN"

# JWT Secret
#It is used to verify user login keeping it here is risky cause hacker can dupliacte the user  
JWT_SECRET = "MASKED_SIGNING_KEY"

# SSH Private Key (partial example)
#This is a digital signature having it here can risk of whole system login without futhure login access
SSH_PRIVATE_KEY = """
-----BEGIN RSA PRIVATE KEY-----
[REMOVED_FOR_SECURITY_REASON]
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