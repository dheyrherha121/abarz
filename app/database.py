from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from .config import setting
SQLALCHEMY_URL = f'postgresql://{setting.database_username}:{setting.database_password}@{setting.database_hostname}:{setting.database_port}/{setting.database_name}'
Base = declarative_base()
engine = create_engine(SQLALCHEMY_URL)
sessionLocal = sessionmaker(autoflush =False,autocommit = False, bind = engine)


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
