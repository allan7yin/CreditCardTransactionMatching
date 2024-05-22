from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..service import rules_service
from ..schema import rules_schema
from ..db import core

router = APIRouter(
    prefix="/rules",
    tags=["rules"],
    responses={404: {"description": "Not found"}},
)


# create rules endpoint
@router.post("/create", response_model=None)
async def create_rules(rulesIn: rules_schema.RuleListIn, db: Session = Depends(core.get_db)):
    try:
        rules_service.create_rules(db=db, rulesIn=rulesIn)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


# get rules endpoint
@router.get("/", response_model=rules_schema.RuleListOut)
async def get_rules(db: Session = Depends(core.get_db)):
    try:
        rules = rules_service.get_rules(db=db)
        return rules
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/healthcheck")
async def healthcheck():
    return "Rules endpoint is healty"
