from fastapi import APIRouter

accounts_router = APIRouter(
    prefix="/accounts",
    tags=["accounts"]
)

@accounts_router.get("/accounts/{id}")
async def accounts_id():
    return {"message": "rota accounts"}


@accounts_router.post("/accounts")
async def accounts():
    return {"message": "rota accounts"}