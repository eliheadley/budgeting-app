from pydantic import BaseModel


class Transaction(BaseModel):
    date:str
    category:str
    merchant:str
    amount:float
    payment_method:str
    notes:str