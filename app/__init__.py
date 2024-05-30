from flask import Flask
from flask_session import Session
from .routes import register_blueprints
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Register blueprints
    register_blueprints(app)

    # Initialize the Flask-Session extension
    Session(app)

    return app
