from .main import bp as main_bp
from .search import bp as search_bp
from .sign_up import bp as signup_bp

def register_blueprints(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(search_bp)
    app.register_blueprint(signup_bp)
 