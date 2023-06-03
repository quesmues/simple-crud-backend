from typing import Optional

from pydantic import UUID4, BaseModel, EmailStr, SecretStr


class Usuario(BaseModel):
    id: Optional[UUID4]
    email: EmailStr
    username: str
    password: SecretStr

    class Config:
        orm_mode = True
