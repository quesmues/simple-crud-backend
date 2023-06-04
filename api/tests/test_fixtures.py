from random import randrange

import pytest


@pytest.fixture
def usuario_fixture() -> dict:
    return {"email": "teste@example.com", "username": "teste", "password": "teste"}


@pytest.fixture
def token_fixture() -> dict:
    return {"access_token": "str", "refresh_token": "str"}


@pytest.fixture
def tokenusuario_fixture() -> dict:
    return {"username": "teste", "email": "teste"}


@pytest.fixture
def tokenpayload_fixture() -> dict:
    return {"exp": 0, "sub": "str"}
