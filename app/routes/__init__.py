from .main import bp as main_bp
from .search import bp as search_bp

def register_blueprints(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(search_bp)
