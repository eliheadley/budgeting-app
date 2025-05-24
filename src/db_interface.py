import sqlite3
from src.environment import app_environment

class DBInterface:

    def __init__(self):
        self.db_name = app_environment.db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.create_table()


    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                category TEXT NOT NULL,
                merchant TEXT NOT NULL,
                amount REAL NOT NULL,
                payment_method TEXT NOT NULL,
                notes TEXT
            )
        ''')
        self.connection.commit()


    def insert_transaction(self, date, category, merchant, amount, payment_method, notes):
        self.cursor.execute('''
            INSERT INTO transactions (date, category, merchant, amount, payment_method, notes)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (date, category, merchant, amount, payment_method, notes))
        self.connection.commit()


    def get_transactions(self):
        self.cursor.execute('SELECT * FROM transactions')
        transactions = self.cursor.fetchall()
        return transactions

db_manager = DBInterface()