from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import UUID4
from sqlalchemy.orm import Session

from api.apps.v1.usuario import schemas, services
from api.config.settings import settings
from api.core.database import get_db

router = APIRouter(prefix="/usuario")


@router.post("/", response_model=schemas.Usuario)
async def create_usuario(usuario: schemas.Usuario, db: Session = Depends(get_db)):
    exists = services.get_usuario_email(db=db, email=usuario.email)
    if exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuário com este email já existe",
        )
    return services.create_usuario(db=db, usuario=usuario)


@router.get("/", response_model=List[schemas.Usuario])
async def list_usuarios(
    offset: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    usuarios = services.get_usuarios(db, offset=offset, limit=limit)
    return usuarios


@router.get("/{usuario_id}", response_model=schemas.Usuario)
async def read_usuario(usuario_id: UUID4, db: Session = Depends(get_db)):
    db_usuario = services.get_usuario(db, usuario_id=usuario_id)
    if db_usuario is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado"
        )
    return db_usuario
