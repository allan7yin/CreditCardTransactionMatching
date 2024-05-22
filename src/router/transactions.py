from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..service import transactions_service
from ..schema import transaction_schema

from ..db import core

router = APIRouter(
    prefix="/transactions",
    tags=["transactions"],
    responses={404: {"description": "Not found"}},
)


# create transaction endpoint
@router.post("/processBatch", response_model=transaction_schema.TransactionOut)
async def process_batch_transactions(
    transactions_raw: transaction_schema.TransactionListIn,
    db: Session = Depends(core.get_db)
):
    try:
        max_points_earned = transactions_service.process_batch_transactions(
            db=db,
            transactions_raw=transactions_raw
        )
        return transaction_schema.TransactionOut(
            points_earned=max_points_earned,
            number_of_transactions=len(transactions_raw.transactions),
        )
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/healthcheck")
async def healthcheck():
    return "Transactions endpoint is healty"
