from fastapi import FastAPI
from .router import transactions, rules
from .db.core import Base, engine
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(transactions.router, prefix="/api/v1")
app.include_router(rules.router, prefix="/api/v1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
async def root():
    return {"message": "Hello! Connection Established"}
