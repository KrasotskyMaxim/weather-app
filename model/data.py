from pydantic import BaseModel


class UserData(BaseModel):
    id: int
    username: str
    password: str
    city: str
    

class WeatherData(BaseModel):
    city: str
    main: str
    description: str
    temp: float
    feels_like: float
    wind_speed: float
    sunrise_time: str
    sunset_time: str
    humidity: int
    icon: str
    current_time: str
