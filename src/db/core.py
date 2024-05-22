from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import typing as t
from sqlalchemy.ext.declarative import declarative_base

import logging

logger = logging.getLogger("uvicorn.info")

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency
def get_db():
  logger.info("=== Database Setup Started ===")
  db = SessionLocal()
  try:
    yield db
  finally:
    logger.info("=== Closing Database Connection ===")
    db.close()