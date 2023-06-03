import uuid

from sqlalchemy import Boolean, Column, String

from api.core.database import Base


class Usuario(Base):
    __tablename__ = "apps_v1_usuario"

    id = Column(String(36), primary_key=True, unique=True, default=uuid.uuid4)
    email = Column(String(256), unique=True, nullable=False)
    username = Column(String(256))
    password = Column(String(256))
    is_active = Column(Boolean, default=True)
