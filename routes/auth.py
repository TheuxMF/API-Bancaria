from fastapi import APIRouter

auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@auth_router.post("/login")
async def login():
    return {"message": "rota auth"}


@auth_router.post("/register")
async def register():
    return {"message": "rota auth"}
