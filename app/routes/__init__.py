from .main import bp as main_bp
from .manual import bp as manual_bp
from .search import bp as search_bp
from .comparative import bp as comparative_bp


def register_blueprints(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(manual_bp)
    app.register_blueprint(search_bp)
    app.register_blueprint(comparative_bp)
 