from fastapi import HTTPException, status

LoginIncorretoException = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Usuário ou senha incorretos",
)
