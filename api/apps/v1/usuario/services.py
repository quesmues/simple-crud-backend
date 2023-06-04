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
