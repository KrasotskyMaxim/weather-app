import settings
from exceptions import (
    LoginException,
    SignInException,
    UpdateProfileException,
    CityException,
)

from model import Database, Api, WeatherData, UserData


class Model:
    '''Model class.'''

    def __init__(self, view):
        self.view = view
        self.db = Database(settings.DB_PATH, settings.CITY_LIST_PATH)
        self.api = Api()
    
    def check_empty_fields(self, mode, *args):
        for field in args:
            if not field:
                if mode == settings.LOGIN_MODE:
                    raise LoginException("All fields must be filled.")
            
    def check_confirm_password(self, mode, password, confirm_password):
        if password != confirm_password:
            if mode == settings.LOGIN_MODE:
                raise LoginException("Passwords do not match.")
    
    def save_user(self, *args):
        self.db.save_user(*args)
        
    def update_user(self, *args):
        try:
            user_id = self.current_user_info.id
            self.db.update_user(user_id, *args)
            self.init_current_user(user_id, *args)
            self.set_profile_weather()
            self.view.goto_home()
        except Exception as e:
            raise UpdateProfileException("Update fields are incorrect!", str(e))
        
    def check_exists_user(self, mode, *args):
        if not (user_info := self.db.get_user(*args)):
            if mode == settings.SIGN_IN_MODE:
                raise SignInException("Invalid username or password.")
        return user_info

    def init_user(self, *args):
        user_info = self.check_exists_user(settings.SIGN_IN_MODE, *args)
        self.init_current_user(*user_info)
        
    def init_current_user(self, *args):
        current_user_info = {
            "id": args[0],
            "username": args[1],
            "password": args[2],
            "city": args[3],
        }
        self.current_user_info = UserData(**current_user_info)
        self.current_city = self.current_user_info.city

    def set_profile_weather(self, city: str = None, refresh: bool = False):
        if not refresh:
            self.current_city = city if city else self.current_user_info.city
        weather_info = self.api.get_city_weather(self.current_city)
        weather_data = WeatherData(**weather_info)
        self.view.home_view.update_weather(weather_data)

    def set_user_profile(self):
        self.view.profile_view.set_user_profile(self.current_user_info)
        
    def check_exists_city(self, city):
        if not self.db.get_city(city):
            raise CityException("City not found.")
