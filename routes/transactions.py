from fastapi import APIRouter, Depends, HTTPException
from dependencies import check_token, get_session
from sqlalchemy.orm import Session
from models import Account, Transaction, User

from dependencies import check_token

transactions_router = APIRouter(
    prefix="/transactions",
    tags=["transactions"],
    dependencies=[Depends(check_token)]
)

@transactions_router.post("/deposit")
async def deposit(session: Session = Depends(get_session), user: User = Depends(check_token), amount: float = 0.0):
    account = session.query(Account).filter(Account.user_id == user.id).first()
    if not account:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    account.balance += amount
    transaction = Transaction(account_id=account.id, type_transaction="deposit", amount=amount)
    session.add(transaction)
    session.commit()
    return {"message": "Saldo Adicionado com Sucesso"}

@transactions_router.post("/withdraw")
async def withdraw(session: Session = Depends(get_session), user: User = Depends(check_token), amount: float = 0.0):
    account = session.query(Account).filter(Account.user_id == user.id).first()
    if not account:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    if account.balance < amount:
        raise HTTPException(status_code=400, detail="Saldo insuficiente")
    if amount <= 0:
        raise HTTPException(status_code=400, detail="Valor de saque inválido")
    if account.balance < amount:
        raise HTTPException(status_code=400, detail="Saldo insuficiente")
    account.balance -= amount
    transaction = Transaction(account_id=account.id, type_transaction="withdraw", amount=amount)
    session.add(transaction)
    session.commit()
    return {"message": "Saque realizado com sucesso"}

@transactions_router.get("/statement/{account_id}")
async def statement(session: Session = Depends(get_session), user: User = Depends(check_token)):
    account = session.query(Account).filter(Account.user_id == user.id).first()
    if not account:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    transactions = session.query(Transaction).filter(Transaction.account_id == account.id).all()
    return {"transactions": transactions}

