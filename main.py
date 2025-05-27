from fastapi import FastAPI
from loguru import logger
from src.database.db_interface import sqlite_db
from src.database.querries import SQLiteQuerries
from src.models import Transaction

app = FastAPI()

@app.post('/add-transaction')
def add_transaction(transaction:Transaction):
    sqlite_db.insert(SQLiteQuerries.INSERT_MERCHNAT, (transaction.merchant, transaction.merchant))
    sqlite_db.insert(SQLiteQuerries.INSERT_CATEGORIES, (transaction.category, transaction.category))
    sqlite_db.insert(SQLiteQuerries.INSERT_PAYMENT_METHOD, (transaction.payment_method, transaction.payment_method))
    sqlite_db.insert(SQLiteQuerries.INSERT_TRANSACTION, tuple(transaction.model_dump().values()))
    return 200


@app.get('/get-transactions')
def get_transactions():
    transactions = sqlite_db.select(SQLiteQuerries.SELECT_ALL_TRANSACTIONS)
    logger.info('Successfully pulled transactions from db')
    return [Transaction(**dict(zip(Transaction.model_fields.keys(), data[1:]))) for data in transactions]
