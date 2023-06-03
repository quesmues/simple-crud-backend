from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from passlib.context import CryptContext

from api.config.settings import settings

reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl=settings.prefix_v1 + "/login", scheme_name="JWT"
)

password_context = CryptContext(schemes=["sha512_crypt"], deprecated="auto")


def get_hashed_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)
