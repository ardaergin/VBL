from flask import Flask
from flask_session import Session
from routes import register_blueprints
import os

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_secret_key'
    app.config['SESSION_TYPE'] = 'filesystem'  # Use filesystem-based session storage
    app.config['SESSION_FILE_DIR'] = '/tmp/flask_session/'  # Directory to store session files

    # Register blueprints
    register_blueprints(app)

    # Initialize the Flask-Session extension
    Session(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=False)
