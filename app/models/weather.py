from ..extensions import db
from sqlalchemy.dialects.postgresql import JSONB
from ..config import TIMEZONE
from datetime import datetime

class Weather(db.Model):
    __tablename__ = "weather"
    
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    light = db.Column(JSONB, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(TIMEZONE), index=True)
    stored_at = db.Column(db.DateTime(timezone=True), nullable=False, index=True, default=lambda: datetime.now(TIMEZONE))
    
    def to_dict(self):
        return {
            "id": self.id,
            "temperature": self.temperature,
            "humidity": self.humidity,
            "light": self.light,
            "created_at": self.created_at.isoformat(),
            "stored_at": self.stored_at.isoformat()
        }