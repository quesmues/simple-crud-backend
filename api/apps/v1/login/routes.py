from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from api.apps.v1.login.exceptions import LoginIncorretoException
from api.apps.v1.login.schemas import Token, TokenUsuario
from api.apps.v1.login.services import create_token
from api.apps.v1.usuario import services
from api.config.settings import settings
from api.core.auth import verify_password
from api.core.database import get_db

router = APIRouter(prefix="/login")


@router.post(
    "",
    response_model=Token,
)
async def login(
    form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = await services.get_usuario(db=db, username=form.username)
    if user is None:
        raise LoginIncorretoException

    password_hash = user.password
    if not verify_password(form.password, password_hash):
        raise LoginIncorretoException

    usuario = TokenUsuario.from_orm(user).dict()

    return {
        "access_token": await create_token(
            usuario, minutes=settings.jwt_configs.get("ACCESS_TOKEN_EXPIRE_MINUTES")
        ),
        "refresh_token": await create_token(
            usuario, minutes=settings.jwt_configs.get("REFRESH_TOKEN_EXPIRE_MINUTES")
        ),
    }
