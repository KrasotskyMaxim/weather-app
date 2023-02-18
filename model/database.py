import sqlite3

from exceptions import DBConnectionException


class Database:
    def __init__(self, db_path):
        self.connect_db(db_path)
        
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
        
    def get_user(self, *args):
        self.cur.execute(
            f"""SELECT * FROM User 
                WHERE username = '{args[0]}' AND password = '{args[1]}'"""
        )
        return self.cur.fetchone()
