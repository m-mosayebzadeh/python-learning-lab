from fastapi import FastAPI
from api.git_api import router as git_router

app = FastAPI()
app.include_router(git_router)
