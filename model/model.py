import settings
from exceptions import (
    LoginException,
    SignInException,
)

from model.database import Database


class Model:
    '''Model class.'''
    
    current_user_info = {
        "username": "",
        "password": "",
        "city": "",
    }
    
    def __init__(self, view):
        self.view = view
        self.db = Database(settings.DB_PATH)
    
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
    
    def check_exists_user(self, mode, *args):
        if not (user_info := self.db.get_user(*args)):
            if mode == settings.SIGN_IN_MODE:
                raise SignInException("Invalid username or password.")
        self.init_current_user(user_info)
        
    def init_current_user(self, user_info):
        self.current_user_info["username"] = user_info[1]
        self.current_user_info["password"] = user_info[2]
        self.current_user_info["city"] = user_info[3]
        
    def prepare_home_view(self):
        self.view.update_time()