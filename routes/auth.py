from fastapi import APIRouter, Depends, HTTPException
from models import User
from dependencies import get_session, check_token
from main import bcrypt_context, SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from schemas import UserSchema, LoginSchema
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordRequestForm
import re

auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


def clear_cpf(cpf):
    # Remove tudo que não for dígito
    return re.sub(r'\D', '', str(cpf))

def create_token(id_user, duration_token=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    expiration_date = datetime.now(timezone.utc) + duration_token
    dic_info = {"sub": str(id_user), "exp": expiration_date}
    encode_token = jwt.encode(dic_info, SECRET_KEY, ALGORITHM)
    return encode_token

def authenticate_user(cpf, password, session):
    user = session.query(User).filter(User.cpf == cpf).first()
    if not user:
        return False
    elif not bcrypt_context.verify(password, user.password):
        return False
    return user



@auth_router.post("/register")
async def register(user_schema: UserSchema, session = Depends(get_session)):
    #user = session.query(User).filter(User.cpf == clear_cpf(user_schema.cpf)).first()
    user = session.query(User).filter(User.email==user_schema.email).first()
    if user:
        raise HTTPException(status_code=400, detail="CPF já cadastrado")
    else:
        password_encrypted = bcrypt_context.hash(user_schema.password)
        new_user = User(
            name=user_schema.name,
            cpf=clear_cpf(user_schema.cpf),
            email=user_schema.email,
            password=password_encrypted
        )
        session.add(new_user)
        session.commit()
        return{"message": "Usuario cadastrado"}
    


@auth_router.post("/login")
async def login(login_schema: LoginSchema, session: Session = Depends(get_session)):
    user = authenticate_user(clear_cpf(login_schema.cpf), login_schema.password, session)
    if not user:
        raise HTTPException(status_code=400, detail="Usuario não encontrado, ou credenciais invalidas")
    else:
        access_token = create_token(user.id)
        refresh_token = create_token(user.id, duration_token=timedelta(days=7))
        return{"access_token": access_token,
               "refresh_token": refresh_token,
               "token_type":"Bearer"}
    
@auth_router.post("/login-form")
async def login_form(date_form: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    user = authenticate_user(clear_cpf(date_form.username), date_form.password, session)
    if not user:
        raise HTTPException(status_code=400, detail="Usuario não encontrado, ou credenciais invalidas")
    else:
        access_token = create_token(user.id)
        refresh_token = create_token(user.id, duration_token=timedelta(days=7))
        return{"access_token": access_token,
               "refresh_token": refresh_token,
               "token_type":"Bearer"}

    
@auth_router.get("/refresh")
async def user_refresh_token(user: User = Depends(check_token)):
    access_token = create_token(user.id)

    return{
        "access_token": access_token,
        "token_type":"Bearer"
        }