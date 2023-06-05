import email

from pydantic import UUID4
from sqlalchemy.orm import Session

from api.apps.v1.usuario import models, schemas
from api.core.auth import get_hashed_password


async def get_usuario(db: Session, username: str):
    email = db.query(models.Usuario).filter_by(email=username).first()
    if email:
        return email
    return db.query(models.Usuario).filter_by(username=username).first()


async def get_usuario_by_id(db: Session, usuario_id: str):
    return db.query(models.Usuario).get(usuario_id)


async def delete_usuario_by_id(db: Session, usuario_id: str):
    db_user = db.query(models.Usuario).get(usuario_id)
    db.delete(db_user)
    db.commit()


async def get_usuarios(db: Session, offset: int = 0, limit: int = 100):
    return db.query(models.Usuario).offset(offset).limit(limit).all()


async def create_usuario(db: Session, usuario: schemas.Usuario):
    db_usuario = models.Usuario(
        email=usuario.email,
        username=usuario.username,
        password=get_hashed_password(usuario.password.get_secret_value()),
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


async def patch_usuario(db: Session, user_id: UUID4, usuario: schemas.Usuario):
    db_usuario = models.Usuario(
        id=str(user_id),
        email=usuario.email,
        username=usuario.username,
    )
    if usuario.password.get_secret_value() != "**********":
        db_usuario.password = get_hashed_password(usuario.password.get_secret_value())
    merged = db.merge(db_usuario)
    db.commit()
    return merged
