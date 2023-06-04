from api.apps.v1.usuario.models import Usuario
from api.apps.v1.usuario.schemas import Usuario as Usuario_schema


def test_usuario_model(usuario_fixture):
    db_usuario = Usuario(**usuario_fixture)
    usuario = Usuario_schema.from_orm(db_usuario)

    assert isinstance(usuario, Usuario_schema)
    assert isinstance(db_usuario, Usuario)
