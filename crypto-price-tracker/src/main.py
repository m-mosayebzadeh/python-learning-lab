from fastapi import FastAPI
from api import membership_api, user_api, crypto_api, auth_api
from exception.app_exception import AppException
from fastapi import Request
from fastapi.responses import JSONResponse

app = FastAPI()

app.include_router(membership_api.router)
app.include_router(user_api.router)
app.include_router(crypto_api.router)
app.include_router(auth_api.router)

@app.exception_handler(AppException)
def app_exception_handler(request: Request, exc: AppException) -> JSONResponse:
    return JSONResponse(
        status_code= exc.status_code,
        content= {"detail": exc.detail}
    )