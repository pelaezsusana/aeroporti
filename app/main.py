from fastapi import FastAPI
from app.routers import aeroporti

app = FastAPI()
app.include_router(aeroporti.router)
