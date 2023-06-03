from datetime import datetime, timedelta
from typing import Any, Union

from fastapi import HTTPException, status
from jose import jwt
from pydantic import ValidationError

from api.apps.v1.login.schemas import TokenPayload
from api.config.settings import settings


async def create_token(subject: Union[str, Any], minutes: int) -> str:
    expires_delta = datetime.utcnow() + timedelta(minutes=minutes)

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(
        to_encode,
        settings.jwt_configs.get("JWT_SECRET_KEY"),
        settings.jwt_configs.get("ALGORITHM"),
    )
    return encoded_jwt


async def validate_token(token: str):
    try:
        payload = jwt.decode(
            token,
            settings.jwt_configs.get("JWT_SECRET_KEY"),
            algorithms=[settings.jwt_configs.get("ALGORITHM")],
        )
        token_data = TokenPayload(**payload)

        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expirado",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Não foi possível validar as credenciais",
            headers={"WWW-Authenticate": "Bearer"},
        )
