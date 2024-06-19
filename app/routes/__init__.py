from .main import bp as main_bp

def register_blueprints(app):
    app.register_blueprint(main_bp)
