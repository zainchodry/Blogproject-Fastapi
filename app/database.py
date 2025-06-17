from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

engine = create_engine("postgresql://ali:pgadmin789%40@localhost/mydb7")

Base = declarative_base()

SessionLocal = sessionmaker(bind = engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

