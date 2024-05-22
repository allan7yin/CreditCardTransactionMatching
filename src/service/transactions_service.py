from typing import Dict
from ..schema import transaction_schema

import logging

logger = logging.getLogger('uvicorn.info')

"""
This processes a batch of user transactions, computing maximum earn and returning the value
"""
def process_batch_transactions(transactions_raw: transaction_schema.TransactionListIn):
    logger.info("=== Beginning transaction matching operation ===")

    # create vendor map
    transactions: Dict[str, float] = {}
    for transaction_in in transactions_raw.transactions.values():
        transactions[transaction_in.merchant_code] = (transaction_in.amount_cents / 100)
    
    # perform dp
    EARN_RULES: Dict[str, float] = [
        {"points": 500, "sportcheck": 75, "tim_hortons": 25, "subway": 25},
        {"points": 300, "sportcheck": 75, "tim_hortons": 25},
        {"points": 200, "sportcheck": 75},
        {"points": 150, "sportcheck": 25, "tim_hortons": 10, "subway": 10},
        {"points": 75, "sportcheck": 25, "tim_hortons": 10},
        {"points": 75, "sportcheck": 20},
    ]

    def dp(transactions: Dict[str, float]):
        points = sum(transactions.values())
        for rule in EARN_RULES:
            if validate(rule,transactions):
                cpy = transactions.copy()
                for merchant in cpy.keys():
                    if merchant not in rule:
                        continue
                    cpy[merchant] -= rule[merchant]
                pts = rule["points"] + dp(cpy)
                points = max(pts,points)
        return points
    result = dp(transactions)
    logger.info("=== Max earn on transactions is %d ===", result)
    return result


def validate(rule: Dict[str, float],transaction: Dict[str, float]):
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

