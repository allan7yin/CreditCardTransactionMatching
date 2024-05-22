from fastapi import FastAPI
from .router import transactions

app = FastAPI()
app.include_router(transactions.router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "Hello! Connection Established"}
