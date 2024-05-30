from .main import bp as main_bp
from .search_2 import bp as search_bp
from .sign_up import bp as sign_up_bp

def register_blueprints(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(search_bp)
    app.register_blueprint(sign_up_bp)