from typing import Dict, List
from pydantic import BaseModel

class TransactionIn(BaseModel):
    """
    Represents details of a single transaction
    """
    date: str
    merchant_code: str
    amount_cents: float

class TransactionListIn(BaseModel):
    """
    Represents a Response of Processing of User Transactions for Request Body
    """
    transactions: Dict[str, TransactionIn]

class TransactionOut(BaseModel):
  """
  Represents a Response of Processing List of User Transactions
  """
  points_earned: float
  number_of_transactions: int
