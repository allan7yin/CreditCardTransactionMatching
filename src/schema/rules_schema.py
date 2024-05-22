from typing import Dict, List
from pydantic import BaseModel


class Rule(BaseModel):
    """
    Represents a single rule, represented by key value pair of vendor:offer
    """

    rule: Dict[str, float]


class RuleListIn(BaseModel):
    """
    Represents a List of Rules for Request Body
    """

    rules: List[Rule]


class RuleListOut(BaseModel):
    """
    Represents a Response of Processing of Getting List of Rules
    """

    rules: List[Rule]

