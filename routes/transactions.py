from fastapi import APIRouter, Depends

from dependencies import check_token

transactions_router = APIRouter(
    prefix="/transactions",
    tags=["transactions"],
    dependencies=[Depends(check_token)]
)

@transactions_router.post("/deposit")
async def deposit():
    return {"message": "rota transactions"}

@transactions_router.post("/withdraw")
async def withdraw():
    return {"message": "rota transactions"}

@transactions_router.get("/statement/{account_id}")
async def statement():
    return {"message": "rota transactions"}

