from sqlmodel import SQLModel
from .engine import engine

def init_db_and_tables():
    with engine.begin() as conn:
        SQLModel.metadata.create_all(conn)