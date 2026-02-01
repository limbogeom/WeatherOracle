from .extensions import db
from sqlalchemy.dialects.postgresql import JSONB

class Weather(db.Model):
    __tablename__ = "weather"
    
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    light = db.Column(JSONB, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.func.now())
    stored_at = db.Column(db.DateTime(timezone=True), nullable=False)