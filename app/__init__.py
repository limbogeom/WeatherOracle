from flask import Flask
from .extensions import db, migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    from .routes import weather_bp
    app.register_blueprint(weather_bp)
    
    return app
    
    