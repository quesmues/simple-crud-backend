from api.apps.v1.login.schemas import Token, TokenPayload, TokenUsuario
from api.apps.v1.usuario.models import Usuario


def test_tokenusuario(tokenusuario_fixture):
    db_usuario = Usuario(**tokenusuario_fixture)
    usuario = TokenUsuario.from_orm(db_usuario)

    assert isinstance(usuario, TokenUsuario)
    assert isinstance(db_usuario, Usuario)


def test_token(token_fixture):
    token = Token(**token_fixture)

    assert isinstance(token, Token)


def test_tokenpayload(tokenpayload_fixture):
    token = TokenPayload(**tokenpayload_fixture)

    assert isinstance(token, TokenPayload)
