from fastapi import FastAPI
from loguru import logger
from src.db_interface import db_manager
from src.models import Transaction

app = FastAPI()

@app.post('/add-transaction')
def add_transaction(transaction:Transaction):
    db_manager.insert_transaction(**transaction.model_dump())
    return 200


@app.get('/get-transactions')
def get_transactions():
    transactions = db_manager.get_transactions()
    logger.info('Successfully pulled transactions from db')
    return [Transaction(**dict(zip(Transaction.model_fields.keys(), data[1:]))) for data in transactions]
