import sqlite3
from src.database.querries import SQLiteQuerries
from abc import ABC, abstractmethod
from src.environment import app_environment

class BaseDatabase(ABC):
    @abstractmethod
    def select(self, query: str, params: tuple = ()):
        pass

    @abstractmethod
    def insert(self, query: str, params: tuple = ()):
        pass

    @abstractmethod
    def update(self, query: str, params: tuple = ()):
        pass

    @abstractmethod
    def delete(self, query: str, params: tuple = ()):
        pass

    @abstractmethod
    def execute(self, query: str, params: tuple = ()):
        pass

class SQLiteDatabase(BaseDatabase):

    def __init__(self):
        self.db_name = app_environment.db_name
        self.execute(SQLiteQuerries.CREATE_CATEGORIES_TABLE)
        self.execute(SQLiteQuerries.CREATE_MERCHANTS_TABLE)
        self.execute(SQLiteQuerries.CREATE_PAYMENT_METHODS_TABLE)
        self.execute(SQLiteQuerries.CREATE_TRANSACTIONS_TABLE)

    def _connect(self):
         return sqlite3.connect(self.db_name)

    def insert(self, query: str, params: tuple = ()):
        with self._connect() as conn:
            cursor = conn.execute(query, params)
            conn.commit()
            return cursor.lastrowid

    def select(self, query: str, params: tuple = ()) -> list[tuple]:
        with self._connect() as conn:
            cursor = conn.execute(query, params)
            return cursor.fetchall()
        
    def execute(self, query: str, params: tuple = ()):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
    
    def delete(self, query: str, id: int):
        self.execute(query, (id,))

    def update(self, query: str, params: tuple = ()):
        self.execute(query, params)
        

sqlite_db = SQLiteDatabase()