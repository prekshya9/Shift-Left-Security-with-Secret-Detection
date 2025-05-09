import os
from dotenv import load_dotenv

def main():
    # Load environment variables
    load_dotenv()
    
    # Get AWS credentials (this is just for demonstration)
    aws_secret = os.getenv('AWS_SECRET_ACCESS_KEY')
    
    print('Welcome to the Secret Detection Lab!')
    print('This is a simple application that demonstrates how secrets might be used in code.')
    print('Try running Gitleaks to detect the secret in the .env file!')

if __name__ == '__main__':
    main()