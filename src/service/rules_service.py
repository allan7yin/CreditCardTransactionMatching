from typing import List
from sqlalchemy import delete
from ..schema import rules_schema
from sqlalchemy.orm import Session
from ..model.rule_model import Rule
import json
from pydantic import ValidationError

import logging

logger = logging.getLogger("uvicorn.info")

"""
This creates the rules for the rewards system
"""
def create_rules(db: Session, rulesIn: rules_schema.RuleListIn):
    # upload each rule into the table, convert the rule into JSON and store to sqlite
    db.execute(delete(Rule))
    logger.info("creating rules")
    for rule in rulesIn.rules:
        json_rule = json.dumps(rule.rule)
        db_rule = Rule(
            rule=json_rule
        )
        db.add(db_rule)
        db.commit()
        db.refresh(db_rule)
    return


"""
Gets all rules
"""
def get_rules(db: Session):
    logger.info("getting rules")
    result: List[rules_schema.Rule] = []
    rules_json = db.query(Rule).all()
    # convert each JSON into pydantic model and return
    for rule_json in rules_json:
        try:
            rule_data = json.loads(rule_json.rule)

            # Creating an instance of Rule using the dictionary
            rule_instance = rules_schema.Rule(rule=rule_data)
            result.append(rule_instance)
        except ValidationError as e:
            logger.exception("Validation Error:", e)
    rulesListResponse = rules_schema.RuleListOut(rules=result)
    return rulesListResponse
