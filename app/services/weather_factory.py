from ..models.weather import Weather
from datetime import datetime
from ..config import TIMEZONE

class WeatherFactory:
    @staticmethod
    def create(temperature: float, humidity: float, light: dict, stored_at: datetime = None):
        return Weather(
            temperature=temperature,
            humidity=humidity,
            light=light,
            stored_at=stored_at or datetime.now(TIMEZONE)
        )