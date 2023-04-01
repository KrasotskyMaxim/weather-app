import settings
import requests
from datetime import datetime


class Api:
    
    @staticmethod
    def _convert_time(timestamp):
        return datetime.fromtimestamp(timestamp).strftime("%H:%M")
    
    @staticmethod
    def get_image_file(icon):
        return settings.STATIC_PATH + icon + ".png"

    def get_city_weather(self, city):
        response = requests.get(
            settings.CITY_WEATHER_URL.format(
                domain=settings.DOMAIN, 
                city=city, 
                units=settings.DEFAULT_UNITS, 
                lang=settings.DEFAULT_LANG,
                key=settings.KEY
            )
        )

        geo_json_data = response.json()
        weather_main = geo_json_data["weather"][0]["main"]
        weather_description = geo_json_data["weather"][0]["description"]
        icon = geo_json_data["weather"][0]["icon"]
        temp = geo_json_data["main"]["temp"]
        humidity = geo_json_data["main"]["humidity"]
        feels_like = geo_json_data["main"]["feels_like"]
        wind = geo_json_data["wind"]["speed"]
        sunrise = self._convert_time(geo_json_data["sys"]["sunrise"])
        sunset = self._convert_time(geo_json_data["sys"]["sunset"])

        return {
            "city": city,
            "main": weather_main,
            "description": weather_description,
            "temp": temp,
            "feels_like": feels_like,
            "wind_speed": wind,
            "sunrise_time": sunrise,
            "sunset_time": sunset,
            "humidity": humidity,
            "icon": self.get_image_file(icon),
            "current_time": datetime.now().strftime("%H:%M"),
        }
        
    def get_weather_forecast(self, city, days: int = 5):
        response = requests.get(
            settings.CITY_FORECAST_URL.format(
                domain=settings.DOMAIN,
                city=city,
                units=settings.DEFAULT_UNITS, 
                cnt=days,
                lang=settings.DEFAULT_LANG,
                key=settings.KEY
            )
        )
        
        forecast_city_data = response.json()
        forecast_list = forecast_city_data["list"]
        forecasts = []
        
        for f in forecast_list:
            weather_main = f["weather"][0]["main"]
            weather_description = f["weather"][0]["description"]
            icon = f["weather"][0]["icon"]
            temp = sum(f["temp"].values()) // len(f["temp"])
            humidity = f["humidity"]
            feels_like = sum(f["feels_like"].values()) // len(f["feels_like"])
            wind = f["speed"]
            sunrise = self._convert_time(f["sunrise"])
            sunset = self._convert_time(f["sunset"])
            
            current_time = datetime.fromtimestamp(f["dt"]).strftime("%d/%m/%Y")

            forecasts.append({
                "city": city,
                "main": weather_main,
                "description": weather_description,
                "temp": temp,
                "feels_like": feels_like,
                "wind_speed": wind,
                "sunrise_time": sunrise,
                "sunset_time": sunset,
                "humidity": humidity,
                "icon": self.get_image_file(icon),
                "current_time": current_time,
            })

        return forecasts