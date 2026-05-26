from fastapi import FastAPI
from api.log_api import router as log_router

app = FastAPI()
app.include_router(log_router)