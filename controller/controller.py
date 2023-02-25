import settings

from exceptions import (
    LoginException,
    SignInException,
    UpdateProfileException,
    CityException,
)
from model.model import Model


class Controller:
    def __init__(self, view) -> None:
        self.model = Model(view)
        
    def login(self, username, password, confirm_password, city):
        try:
            self.model.check_empty_fields(settings.LOGIN_MODE, username, password, confirm_password, city)
            self.model.check_confirm_password(settings.LOGIN_MODE, password, confirm_password)
        except LoginException:
            raise

        self.model.save_user(username, password, city)
        
    def sign_in(self, username, password):
        try:
            self.model.init_user(username, password)
            self.model.set_profile_weather()
        except SignInException:
            raise
        
    def refresh_weather(self):
        self.model.set_profile_weather(refresh=True)
        
    def prepare_profile(self):
        self.model.set_user_profile()
        
    def save_profile(self, username, password, city):
        try:
            self.model.update_user(username, password, city)
        except UpdateProfileException:
            raise
        
    def search_city(self, city):
        try:
            self.model.check_exists_city(city)
            self.model.set_profile_weather(city)
        except CityException as e:
            raise e