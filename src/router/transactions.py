from fastapi import APIRouter, HTTPException

from ..service import transactions_service
from ..schema import transaction_schema

router = APIRouter(
    prefix="/transactions",
    tags=["transactions"],
    responses={404: {"description": "Not found"}},
)

# create transaction endpoint
@router.post("/processBatch", response_model=transaction_schema.TransactionOut)
async def processBatchTransactions(transactions_raw: transaction_schema.TransactionListIn):
    try:
        max_points_earned = transactions_service.process_batch_transactions(transactions_raw)
        return transaction_schema.TransactionOut(
            points_earned=max_points_earned,
            number_of_transactions=len(transactions_raw.transactions)
        )
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

@router.post("/")
async def test():
    print("hello world")
