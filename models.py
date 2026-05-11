from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime, timezone

#Criar conexão do banco
db = create_engine("sqlite:///banco.db")
#Criar a base do banco de dados
Base = declarative_base()
# criar as classe/tabelas do banco

class User(Base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String)
    cpf = Column("cpf", String, unique=True)
    email = Column("email", String, unique=True)
    password = Column("password", String)
    status = Column("status", Boolean, default=True)
    created_at = Column("created_at", DateTime, default=lambda: datetime.now(timezone.utc))

    
    def __init__(self, name, cpf,email,password,status=True):
        self.name = name
        self.cpf = cpf
        self.email = email
        self.password = password
        self.status = status

class Account(Base):
    __tablename__ = "accounts"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    user_id = Column("user_id" ,ForeignKey("users.id"))
    balance = Column(Float, default=0.0)
    type_account = Column("type_account", String) # ("Conta Corrente", "Conta Poupança", "Conta Salario")
    transactions = relationship("Transaction", back_populates="account", cascade="all, delete")
    created_at = Column("created_at", DateTime, default=lambda: datetime.now(timezone.utc))


    def __init__(self, balance,type_account):
        self.balance = balance
        self.type_account = type_account

class Transaction(Base):
    __tablename__="transactions"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    account_id = Column("account_id" ,ForeignKey("accounts.id"))
    type_transaction = Column("type_transaction", String)
    amount = Column("amount", Float)
    created_at = Column("created_at", DateTime, default=lambda: datetime.now(timezone.utc))

    def __init__(self, type_transaction, amount):
        self.type_transaction = type_transaction
        self.amount = amount

# alembic init alembic

# criar a migração: alembic revision --autogenerate -m "menssagem"

# executar a migração: alembic upgrade head