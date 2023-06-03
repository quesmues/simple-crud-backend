from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.apps.v1.login.routes import router as login_v1
from api.apps.v1.usuario.routes import router as usuario_v1
from api.config.settings import settings

app = FastAPI(debug=settings.debug, title="Simple Crud Python", version="0.0.1")

app.include_router(usuario_v1, prefix=settings.prefix_v1)
app.include_router(login_v1, prefix=settings.prefix_v1)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.cors_allow_origins],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
