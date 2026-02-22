from flask import Flask, redirect
from .extensions import db, migrate
from .config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    from .routes.weather_routes import weather_bp
    app.register_blueprint(weather_bp)
    
    @app.get("/")
    def redr():
        return redirect("/api/weather/frontend")
    
    return app
    
    