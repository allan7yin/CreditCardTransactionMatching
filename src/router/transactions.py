from fastapi import APIRouter, HTTPException

from ..service import transactions_service
from ..schema import transaction_schema

router = APIRouter(
    prefix="/transactions",
    tags=["transactions"],
    responses={404: {"description": "Not found"}},
)

# create vendor endpoint
@router.post("/processBatch", response_model=int)
async def processBatchTransactions(transactions_raw: transaction_schema.TransactionListIn):
    try:
        max_points_earned = transactions_service.process_batch_transactions(transactions_raw)
        return 0
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

@router.post("/")
async def test():
    print("hello world")
