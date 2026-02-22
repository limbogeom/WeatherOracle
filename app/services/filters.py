from enum import Enum
from abc import ABC, abstractmethod
from ..models.weather import Weather

class Filter(ABC):
    @abstractmethod
    def apply(self, query, value):
        pass
    
class TempGreaterFilter(Filter):
    def apply(self, query, value):
        return query.filter(Weather.temperature > value)
    
class TempLessFilter(Filter):
    def apply(self, query, value):
        return query.filter(Weather.temperature < value)
    
class HumGreaterFilter(Filter):
    def apply(self, query, value):
        return query.filter(Weather.humidity > value)
    
class HumLessFilter(Filter):
    def apply(self, query, value):
        return query.filter(Weather.humidity < value)
    
class LuxGreaterFilter(Filter):
    def apply(self, query, value):
        return query.filter(Weather.light["lux"].as_float() > value)
    
class LuxLessFilter(Filter):
    def apply(self, query, value):
        return query.filter(Weather.light["lux"].as_float() < value)
    
class MethodFilter(Filter):
    def apply(self, query, value):
        return query.filter(Weather.light["method"].as_text() == value)
    
class FromDateFilter(Filter):
    def apply(self, query, value):
        return query.filter(Weather.stored_at >= value)
    
class ToDateFilter(Filter):
    def apply(self, query, value):
        return query.filter(Weather.stored_at <= value)
    

class FilterType(Enum):
    GREATER_TEMPERATURE = "temp_gt"
    LESS_TEMPERATURE = "temp_lt"
    GREATER_HUMIDITY = "hum_gt"
    LESS_HUMIDITY = "hum_lt"
    GREATER_LUX = "lux_gt"
    LESS_LUX = "lux_lt"
    METHOD = "method"
    TO_DATE = "to_dt"
    FROM_DATE = "from_dt"
    
FILTER_MAP = {
    FilterType.GREATER_TEMPERATURE: TempGreaterFilter(),
    FilterType.LESS_TEMPERATURE: TempLessFilter(),
    FilterType.GREATER_HUMIDITY: HumGreaterFilter(),
    FilterType.LESS_HUMIDITY: HumLessFilter(),
    FilterType.GREATER_LUX: LuxGreaterFilter(),
    FilterType.LESS_LUX: LuxLessFilter(),
    FilterType.METHOD: MethodFilter(),
    FilterType.FROM_DATE: FromDateFilter(),
    FilterType.TO_DATE: ToDateFilter(),
}