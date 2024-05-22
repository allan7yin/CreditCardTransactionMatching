from fastapi import FastAPI
from .router import transactions
from dotenv import load_dotenv
import uvicorn


load_dotenv()

app = FastAPI()
app.include_router(transactions.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Hello! Connection Established"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
