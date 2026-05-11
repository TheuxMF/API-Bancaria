#uvicorn main:app --reload

from fastapi import FastAPI

from routes.auth import auth_router
from routes.accounts import accounts_router
from routes.transactions import transactions_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(accounts_router)
app.include_router(transactions_router)