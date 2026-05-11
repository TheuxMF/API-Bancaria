from fastapi import APIRouter, Depends
from dependencies import check_token


accounts_router = APIRouter(
    prefix="/accounts",
    tags=["accounts"],
    dependencies=[Depends(check_token)]
)

@accounts_router.get("/accounts/{id}")
async def accounts_id():
    return {"message": "rota accounts"}


@accounts_router.post("/accounts")
async def accounts():
    return {"message": "rota accounts"}