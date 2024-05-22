from fastapi import FastAPI
from .router import transactions, rules
from .db.core import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(transactions.router, prefix="/api/v1")
app.include_router(rules.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Hello! Connection Established"}
