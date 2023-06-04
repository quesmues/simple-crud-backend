from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from apps.v1.login.routes import login
from fastapi.security import OAuth2PasswordRequestForm

from api.apps.v1.usuario.models import Usuario


@patch("apps.v1.login.routes.verify_password")
@patch("apps.v1.login.routes.services")
@pytest.mark.asyncio
async def test_login(services_mock, verify_mock):
    form = OAuth2PasswordRequestForm(username="teste", password="teste", scope="")
    db = MagicMock()
    verify_mock.return_value = True
    get_usuario = AsyncMock(
        return_value=Usuario(
            username="teste", password="teste", email="teste@teste.com"
        )
    )
    services_mock.get_usuario = get_usuario
    resp = await login(form, db)

    assert isinstance(resp, dict)
    assert isinstance(resp["access_token"], str)
    assert isinstance(resp["refresh_token"], str)
