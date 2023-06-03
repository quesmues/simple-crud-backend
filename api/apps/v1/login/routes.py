from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from api.apps.v1.login.schemas import Token
from api.apps.v1.usuario import services
from api.config.auth import create_access_token, create_refresh_token, verify_password
from api.config.settings import settings
from api.core.database import get_db

router = APIRouter(prefix="/login")


@router.post(
    "/",
    response_model=Token,
)
async def login(
    form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = services.get_usuario(form.usuario, None)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password",
        )

    hashed_pass = user["password"]
    if not verify_password(form.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password",
        )

    return {
        "access_token": create_access_token(user["email"]),
        "refresh_token": create_refresh_token(user["email"]),
    }
