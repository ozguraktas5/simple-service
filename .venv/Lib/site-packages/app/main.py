from fastapi import FastAPI
from .api import router as api_router

app = FastAPI(title="Simple Service", version="0.1.0")

app.include_router(api_router, prefix="/api")