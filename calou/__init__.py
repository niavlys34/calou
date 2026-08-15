from flask import Flask

def create_app():
    app = Flask(__name__)

    from .main import bp as main_bp
    from .meteo import bp as meteo_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(meteo_bp, url_prefix="/meteo")

    return app
