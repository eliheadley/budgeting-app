from src.db_interface import db_manager
from datetime import date
from src.models import Transaction

def main():
    args = {
        "date": date.today(),
        "category":"Medical",
        "merchant":"Ideal Dental",
        'amount':350.00,
        'payment_method':"Credit",
        'notes':""
    }

    transactions = db_manager.get_transactions()
    print(transactions)
    result = [Transaction(**dict(zip(Transaction.model_fields.keys(), data[1:]))) for data in transactions]
    print(result)


if __name__ == '__main__':
    main()