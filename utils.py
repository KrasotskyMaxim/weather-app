import datetime
import requests
import settings


def convert_time(timestamp: int) -> str:
    return datetime.datetime.fromtimestamp(timestamp).strftime("%H:%M")


def get_image_file(icon: str):
    return settings.STATIC_PATH + icon + ".png"


def get_city_geo(
    domain: str = settings.DOMAIN,
    city: str = settings.DEFAULT_CITY, 
    limit: int = 1,
    key: str = settings.KEY  
):
    response = requests.get(
        settings.CITY_GEO_URL.format(
            domain=domain, 
            city=city, 
            limit=limit, 
            key=key
            )
        )

    city_json_data = response.json()[0]
    city_lat, city_lon = city_json_data["lat"] , city_json_data["lon"]

    return city_lat, city_lon


def get_city_weather(
    domain: str = settings.DOMAIN,
    city: str = settings.DEFAULT_CITY,
    units: str = settings.DEFAULT_UNITS,
    lang: str = settings.DEFAULT_LANG,
    key: str = settings.KEY
):
    response = requests.get(
        settings.CITY_WEATHER_URL.format(
            domain=domain, 
            city=city, 
            units=units, 
            lang=lang,
            key=key
            )
        )

    geo_json_data = response.json()
    weather = geo_json_data["weather"][0]["description"]
    icon = geo_json_data["weather"][0]["icon"]
    temp = geo_json_data["main"]["temp"]
    feels_like = geo_json_data["main"]["feels_like"]
    wind = geo_json_data["wind"]["speed"]
    sunrise = convert_time(geo_json_data["sys"]["sunrise"])
    sunset = convert_time(geo_json_data["sys"]["sunset"])

    return weather, temp, feels_like, wind, sunrise, sunset, icon


def get_geo_weather(
    domain: str = settings.DOMAIN,
    city: str = settings.DEFAULT_CITY,
    units: str = settings.DEFAULT_UNITS,
    lang: str = settings.DEFAULT_LANG,
    key: str = settings.KEY
):
    lat, lon = get_city_geo(city=city)
    response = requests.get(
        settings.GEO_WEATHER_URL.format(
            domain=domain, 
            lat=lat, 
            lon=lon, 
            units=units, 
            lang=lang,
            key=key
            )
        )

    geo_json_data = response.json()
    weather = geo_json_data["weather"][0]["description"]
    icon = geo_json_data["weather"][0]["icon"]
    temp = geo_json_data["main"]["temp"]
    feels_like = geo_json_data["main"]["feels_like"]
    wind = geo_json_data["wind"]["speed"]
    sunrise = convert_time(geo_json_data["sys"]["sunrise"])
    sunset = convert_time(geo_json_data["sys"]["sunset"])

    return weather, temp, feels_like, wind, sunrise, sunset, icon


def get_city_forecast(
    domain: str = settings.DOMAIN,
    city: str = settings.DEFAULT_CITY,
    units: str = settings.DEFAULT_UNITS,
    cnt: int = 7,
    key: str = settings.KEY
):
    response = requests.get(
        settings.CITY_FORECAST_URL.format(
            domain=domain, 
            city=city, 
            units=units, 
            cnt=cnt,
            key=key
            )
        )

    forecast_json_data = response.json()
    forecast_list = forecast_json_data["list"]
    forecast = []
    for day in forecast_list:
        forecast.append(
            {
                "date": datetime.datetime.fromtimestamp(day["dt"]).strftime("%d %B"),
                "temp": day["temp"]["day"],
                "feels_like": day["feels_like"]["day"],
                "wind": day["speed"],
                "icon": day["weather"][0]["icon"],
            }
        )

    return forecast


def get_geo_forecast(
    domain: str = settings.DOMAIN,
    city: str = settings.DEFAULT_CITY,
    units: str = settings.DEFAULT_UNITS,
    cnt: int = 7,
    key: str = settings.KEY
):
    lat, lon = get_city_geo(city=city)
    response = requests.get(
        settings.GEO_FORECAST_URL.format(
            domain=domain, 
            lat=lat, 
            lon=lon, 
            units=units, 
            cnt=cnt,
            key=key
            )
        )

    forecast_json_data = response.json()
    forecast_list = forecast_json_data["list"]
    forecast = []
    for day in forecast_list:
        forecast.append(
            {
                "date": datetime.datetime.fromtimestamp(day["dt"]).strftime("%d %B"),
                "temp": day["temp"]["day"],
                "feels_like": day["feels_like"]["day"],
                "wind": day["speed"],
                "icon": day["weather"][0]["icon"],
            }
        )

    return forecast
