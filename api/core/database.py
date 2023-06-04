from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from api.config.settings import settings

engine = create_engine(settings.sqlalchemy_db_url)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
