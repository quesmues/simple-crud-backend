from unittest.mock import MagicMock

import pytest

from api.apps.v1.usuario.models import Usuario
from api.apps.v1.usuario.schemas import Usuario as UsuarioSchema
from api.apps.v1.usuario.services import (
    create_usuario,
    get_usuario,
    get_usuario_by_id,
    get_usuarios,
)


@pytest.mark.asyncio
async def test_get_usuario():
    db = MagicMock()
    db_usuario = await get_usuario(db, "teste")

    assert db_usuario


@pytest.mark.asyncio
async def test_get_usuario_by_id():
    db = MagicMock()
    db_usuario = await get_usuario_by_id(db, "teste")

    assert db_usuario


@pytest.mark.asyncio
async def test_get_usuarios():
    db = MagicMock()
    db_usuario = await get_usuarios(db)

    assert db_usuario


@pytest.mark.asyncio
async def test_create_usuario(usuario_fixture):
    usuario = UsuarioSchema(**usuario_fixture)
    db = MagicMock()
    db_usuario = await create_usuario(db, usuario)

    assert isinstance(db_usuario, Usuario)
