import pytest

from api.apps.v1.login.services import create_token, validate_token


@pytest.mark.asyncio
async def test_token():
    token = await create_token("teste", 10)
    await validate_token(token)

    assert isinstance(token, str)
