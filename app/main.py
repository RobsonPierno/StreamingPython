from fastapi import FastAPI
from app.api.v1.endpoints import netflix

app = FastAPI()

app.include_router(netflix.router, prefix="/netflix")
