from typing import List
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from api.apps.v1.usuario.models import Usuario
from api.apps.v1.usuario.routes import create_usuario, list_usuarios, read_usuario
from api.apps.v1.usuario.schemas import Usuario as UsuarioSchema


@patch("api.apps.v1.usuario.routes.services")
@patch("api.apps.v1.usuario.routes.validate_token")
@pytest.mark.asyncio
async def test_create_usuario(validate_token_mock, services_mock, usuario_fixture):
    token = AsyncMock()
    usuario = UsuarioSchema(**usuario_fixture)
    db = MagicMock()
    create_usuario_mock = AsyncMock(return_value=Usuario(**usuario_fixture))
    get_usuario = AsyncMock(return_value=None)
    services_mock.get_usuario = get_usuario
    services_mock.create_usuario = create_usuario_mock
    resp = await create_usuario(usuario, db, token)

    assert isinstance(resp, Usuario)


@patch("api.apps.v1.usuario.routes.services")
@patch("api.apps.v1.usuario.routes.validate_token")
@pytest.mark.asyncio
async def test_list_usuarios(validate_token_mock, services_mock, usuario_fixture):
    token = AsyncMock()
    usuario = UsuarioSchema(**usuario_fixture)
    db = MagicMock()
    get_usuarios = AsyncMock(return_value=[Usuario(**usuario_fixture)])
    services_mock.get_usuarios = get_usuarios
    resp = await list_usuarios(usuario, db, token)

    assert isinstance(resp, List)
    assert isinstance(resp[0], Usuario)


@patch("api.apps.v1.usuario.routes.services")
@patch("api.apps.v1.usuario.routes.validate_token")
@pytest.mark.asyncio
async def test_read_usuario(validate_token_mock, services_mock, usuario_fixture):
    token = AsyncMock()
    db = MagicMock()
    get_usuario_by_id = AsyncMock(return_value=Usuario(**usuario_fixture))
    services_mock.get_usuario_by_id = get_usuario_by_id
    resp = await read_usuario("0", db, token)

    assert isinstance(resp, Usuario)
