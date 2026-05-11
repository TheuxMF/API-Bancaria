from pydantic import BaseModel
from typing import Optional


class UserSchema(BaseModel):
    name: str
    cpf: str
    email: str
    password: str
    status: Optional[bool]

    class config:
        from_attributes = True


class LoginSchema(BaseModel):
    cpf: str
    password: str

    class config:
        from_attributes = True     

class AccountSchema(BaseModel):
    type_account: str

    class config:
        from_attributes = True