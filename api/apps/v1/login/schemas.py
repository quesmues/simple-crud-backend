from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    refresh_token: str


class TokenUsuario(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True


class TokenPayload(BaseModel):
    exp: int
    sub: str
