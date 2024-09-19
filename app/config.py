import os
from dotenv import load_dotenv
from datetime import timedelta

# Load environment variables from .env file
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SESSION_TYPE = os.getenv('SESSION_TYPE')
    SESSION_FILE_DIR = os.getenv('SESSION_FILE_DIR')
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = os.getenv('SESSION_COOKIE_SECURE', 'false').strip().lower() in ['true', '1', 't']
    SESSION_COOKIE_SAMESITE = os.getenv('SESSION_COOKIE_SAMESITE', 'Lax')
    SESSION_LIFETIME = timedelta(days=1)

    FLASK_ENV = os.getenv('FLASK_ENV')
    DEBUG = os.getenv('FLASK_DEBUG', 'false').strip().lower() in ['true', '1', 't']
