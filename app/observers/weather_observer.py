
class WeatherLogger:
    def update(self, weather):
        print(f"[LOG] New Weather entry: Temp={weather.temperature}, Humidity={weather.humidity}, Lux={weather.light.get("lux")}")