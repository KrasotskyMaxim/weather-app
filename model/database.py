import sqlite3
import json

from exceptions import DBConnectionException


class Database:
    def __init__(self, db_path, city_list_path):
        self.connect_db(db_path)
        self.city_list = self.prepare_city_list(city_list_path)
        
    def prepare_city_list(self, path):
        with open(path, 'r') as f:
            data = json.load(f)
        return data
        
    def connect_db(self, db_path):
        try:
            print("connect to db...")
            self.conn = sqlite3.connect(db_path)
            self.cur = self.conn.cursor()
            print("connection success!")
        except sqlite3.Error:
            raise DBConnectionException("connection error!")
    
    def save_user(self, *args):
        self.cur.execute(
            f"""INSERT INTO User (username, password, city) 
                VALUES ('{args[0]}', '{args[1]}', '{args[2]}')"""
        )
        self.conn.commit()
        
    def update_user(self, user_id, *args):
        self.cur.execute(
            f"""UPDATE User 
                SET username = '{args[0]}', password = '{args[1]}', city = '{args[2]}'
                WHERE id = {user_id}"""
        )
        self.conn.commit()
        
    def get_user(self, *args):
        self.cur.execute(
            f"""SELECT * FROM User 
                WHERE username = '{args[0]}' AND password = '{args[1]}'"""
        )
        return self.cur.fetchone()
    
    def get_city(self, city):
        return city in self.city_list