from flask import Flask
from routes import register_blueprints
import os

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_secret_key'

    # Register blueprints
    register_blueprints(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)