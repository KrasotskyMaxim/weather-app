import os
from dotenv import load_dotenv

load_dotenv()

KEY=os.getenv("KEY")
DOMAIN=os.getenv("DOMAIN")
DB_PATH=os.getenv("DB_PATH")
CITY_LIST_PATH=os.getenv("CITY_LIST_PATH")

DEFAULT_LANG="en"
DEFAULT_CITY="Minsk"
DEFAULT_UNITS="metric"

STATIC_PATH="./images/"

LOGIN_MODE = "login"
SIGN_IN_MODE = "sign_in"

CITY_GEO_URL = "{domain}/geo/1.0/direct?q={city}&limit={limit}&appid={key}"
GEO_WEATHER_URL="{domain}/data/2.5/weather?lat={lat}&lon={lon}&units={units}&lang={lang}&appid={key}"
CITY_WEATHER_URL="{domain}/data/2.5/weather?q={city}&units={units}&lang={lang}&appid={key}"
CITY_FORECAST_URL="{domain}/data/2.5/forecast/daily?q={city}&units={units}&cnt={cnt}&appid={key}"
GEO_FORECAST_URL="{domain}/data/2.5/forecast/daily?lat={lat}&lon={lon}&units={units}&cnt={cnt}&appid={key}"
