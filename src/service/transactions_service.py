from typing import Dict
from ..schema import transaction_schema
from ..service.rules_service import get_rules
from sqlalchemy.orm import Session

import logging

logger = logging.getLogger("uvicorn.info")

"""
This processes a batch of user transactions, computing maximum earn and returning the value
"""


def process_batch_transactions(db: Session, transactions_raw: transaction_schema.TransactionListIn):
    logger.info("=== Beginning transaction matching operation ===")

    # create vendor map
    transactions: Dict[str, float] = {}
    for transaction_in in transactions_raw.transactions.values():
        transactions[transaction_in.merchant_code] = transaction_in.amount_cents / 100

    # perform dp
    earn_rules = get_rules(db=db)

    # Extracting a list of Python dictionaries from the raw rules
    cleaned_rules = []
    raw_rules = earn_rules.rules
    for rule in raw_rules:
        cleaned_rules.append(rule.rule)

    def dp(transactions: Dict[str, float]):
        points = sum(transactions.values())
        for rule in cleaned_rules:
            if validate(rule, transactions):
                cpy = transactions.copy()
                for merchant in cpy.keys():
                    if merchant not in rule:
                        continue
                    cpy[merchant] -= rule[merchant]
                pts = rule["points"] + dp(cpy)
                points = max(pts, points)
        return points

    result = dp(transactions)
    logger.info("=== Max earn on transactions is %d ===", result)
    return result


def validate(rule: Dict[str, float], transaction: Dict[str, float]):
    for merchant in rule.keys():
        if merchant == "points":
            continue
        # make sure cannot earn on invalid merchants
        if merchant not in transaction.keys():
            return False
        # make sure cannot earn if transaction does not meet required amount
        if transaction[merchant] < rule[merchant]:
            return False
    return True
