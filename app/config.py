import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    SESSION_TYPE = 'filesystem'
    SESSION_FILE_DIR = '/tmp/flask_session/'
