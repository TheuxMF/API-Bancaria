from fastapi import APIRouter, Depends, HTTPException
from dependencies import check_token
from models import User, Account
from schemas import AccountSchema
from dependencies import get_session
from sqlalchemy.orm import Session

accounts_router = APIRouter(
    prefix="/accounts",
    tags=["accounts"],
    dependencies=[Depends(check_token)]
)

@accounts_router.get("/accounts/{id}")
async def accounts_id(session: Session = Depends(get_session), user: User = Depends(check_token)):
    accounts = session.query(Account).filter(Account.user_id == user.id).all()
    if not accounts:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    return accounts


@accounts_router.post("/accounts")
async def accounts(account_schema: AccountSchema, 
                   session: Session = Depends(get_session),
                   user: User = Depends(check_token)):
    accounts = Account(type_account=account_schema.type_account)
    accounts.user_id = user.id
    session.add(accounts)
    session.commit()
    
    return {"mensagem": "Conta criada com sucesso"}
    