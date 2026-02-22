from ..models.weather import Weather
from .weather_factory import WeatherFactory
from .filters import FilterType, FILTER_MAP
from ..extensions import db



class WeatherService:
    def __init__(self):
        self.observers = []
        
    def subscribe(self, observer):
        self.observers.append(observer)
        
    def notify(self, weather):
        for obs in self.observers:
            obs.update(weather)
            
    def create(self, temperature: float, humidity: float, light: dict, stored_at = None):
        weather = WeatherFactory.create(temperature, humidity, light, stored_at)
        db.session.add(weather)
        db.session.commit()
        self.notify(weather)
        return weather
    
    def get_all(self, filters: dict = None, limit: int = 100):
        q = Weather.query
        
        if filters:
            for key, value in filters.items():
                try:
                    filter_type = FilterType(key)
                    strategy = FILTER_MAP.get(filter_type)
                    if strategy:
                        q = strategy.apply(q, value)
                except ValueError:
                    continue
                
        return q.order_by(Weather.stored_at.desc()).limit(min(limit, 1000)).all()
    
    def get(self, weather_id: int):
        return Weather.query.get_or_404(weather_id)
    
    def delete(self, weather_id: int):
        weather = self.get(weather_id)
        db.session.delete(weather)
        db.session.commit()
    
    def delete_all(self):
        db.session.query(Weather).delete()
        db.session.commit()
    
