from sqlalchemy.orm import Session

from api.apps.v1.usuario import models, schemas
from api.config.auth import get_hashed_password


async def get_usuario(db: Session, usuario_id: int):
    return db.query(models.Usuario).get(usuario_id)


async def get_usuario_email(db: Session, email: str):
    return db.query(models.Usuario).get(email)


async def get_usuarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Usuario).offset(skip).limit(limit).all()


async def create_usuario(db: Session, usuario: schemas.Usuario):
    db_usuario = models.Usuario(
        username=usuario.username, password=get_hashed_password(usuario.password)
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario
