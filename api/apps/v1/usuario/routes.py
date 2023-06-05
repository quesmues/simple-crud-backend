from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response, status
from pydantic import UUID4
from sqlalchemy.orm import Session

from api.apps.v1.login.services import validate_token
from api.apps.v1.usuario import schemas, services
from api.apps.v1.usuario.exceptions import UsuarioNaoEncontradoException
from api.config.settings import settings
from api.core.auth import reuseable_oauth
from api.core.database import get_db

router = APIRouter(prefix="/usuario")

USER_NOT_FOUND = "Usuário não encontrado"


@router.post("/", response_model=schemas.Usuario)
async def create_usuario(
    usuario: schemas.Usuario,
    db: Session = Depends(get_db),
    token: str = Depends(reuseable_oauth),
):
    await validate_token(token)
    exists = await services.get_usuario(db=db, username=usuario.email)
    if exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuário com este email já existe",
        )
    return await services.create_usuario(db=db, usuario=usuario)


@router.patch("/{usuario_id}", response_model=schemas.Usuario)
async def patch_usuario(
    usuario_id: UUID4,
    usuario: schemas.Usuario,
    db: Session = Depends(get_db),
    token: str = Depends(reuseable_oauth),
):
    await validate_token(token)
    db_usuario = await services.get_usuario_by_id(db, usuario_id=usuario_id)
    if db_usuario is None:
        raise UsuarioNaoEncontradoException()
    return await services.patch_usuario(db, usuario_id, usuario)


@router.get("/", response_model=List[schemas.Usuario])
async def list_usuarios(
    offset: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    token: str = Depends(reuseable_oauth),
):
    await validate_token(token)
    usuarios = await services.get_usuarios(db, offset=offset, limit=limit)
    return usuarios


@router.get("/{usuario_id}", response_model=schemas.Usuario)
async def read_usuario(
    usuario_id: UUID4,
    db: Session = Depends(get_db),
    token: str = Depends(reuseable_oauth),
):
    await validate_token(token)
    db_usuario = await services.get_usuario_by_id(db, usuario_id=usuario_id)
    if db_usuario is None:
        raise UsuarioNaoEncontradoException()
    return db_usuario


@router.delete("/{usuario_id}")
async def delete_usuario(
    usuario_id: UUID4,
    db: Session = Depends(get_db),
    token: str = Depends(reuseable_oauth),
):
    await validate_token(token)
    db_usuario = await services.get_usuario_by_id(db, usuario_id=usuario_id)
    if db_usuario is None:
        raise UsuarioNaoEncontradoException()
    await services.delete_usuario_by_id(db, usuario_id=usuario_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
