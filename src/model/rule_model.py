from sqlalchemy import Column, JSON, Integer
from sqlalchemy.orm import relationship
from ..db.core import Base

class Rule(Base):
    """
    Represents an Rule Construct SQLAlchemy Model
    """

    __tablename__ = "rules"
    id = Column(Integer, primary_key=True, index=True)
    rule = Column(JSON)