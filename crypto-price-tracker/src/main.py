from fastapi import FastAPI
from api import membership_api, user_api


app = FastAPI()

app.include_router(membership_api.router)
app.include_router(user_api.router)