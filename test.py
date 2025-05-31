from src.database.db_interface import sqlite_db
from src.database.querries import SQLiteQuerries
from datetime import date
from src.models import Transaction

def main():
    data = {
        "date": '05-24-2025',
        "category":"Medical",
        "merchant":"Ideal Dental",
        'amount':350.00,
        'payment_method':"Credit",
        'notes':""
    }
    transaction = Transaction(**data)
    
    transactions = sqlite_db.select(SQLiteQuerries.SELECT_ALL_TRANSACTIONS)
    print(transactions)


if __name__ == '__main__':
    main()