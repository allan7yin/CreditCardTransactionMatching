from uuid import UUID
from ..schema import transaction_schema

import logging

logger = logging.getLogger(__name__)  # Get logger for current module

"""
This processes a batch of user transactions, computing maximum earn and returning the value
"""
def process_batch_transactions(transactions_raw: transaction_schema.TransactionListIn):
    # first, remove date of transaction to construct vendor amount map
    transactions = {}
    for transaction_in in transactions_raw.transactions.values():
        transactions[transaction_in.merchant_code] = (transaction_in.amount_cents / 100)
    
    # perform dp
    rules = [
        {"points": 500, "sportcheck": 75, "tim_hortons": 25, "subway": 25},
        {"points": 300, "sportcheck": 75, "tim_hortons": 25},
        {"points": 200, "sportcheck": 75},
        {"points": 150, "sportcheck": 25, "tim_hortons": 10, "subway": 10},
        {"points": 75, "sportcheck": 25, "tim_hortons": 10},
        {"points": 75, "sportcheck": 20},
    ]
    def dp(transactions):
        points = sum(transactions.values())
        for rule in rules:
            if validate(rule,transactions):
                cpy = transactions.copy()
                for merchant in cpy.keys():
                    if merchant not in rule:
                        continue
                    cpy[merchant] -= rule[merchant]
                pts = rule["points"] + dp(cpy)
                points = max(pts,points)
        return points
    ans = dp(transactions)
    print(ans)
    return ans


def validate(rule,transaction):
    for merchant in rule.keys():
        if merchant == "points":
            continue
        if merchant not in transaction.keys():
            return False
        if transaction[merchant] < rule[merchant]:
            return False
    return True

