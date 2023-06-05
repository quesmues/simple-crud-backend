from fastapi import HTTPException, status

UsuarioNaoEncontradoException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Usuário não encontrado",
)
