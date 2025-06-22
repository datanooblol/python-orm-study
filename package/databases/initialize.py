from sqlmodel import SQLModel
from .engine import engine
from sqlmodel import text

with engine.connect() as conn:
    conn.execute(text('CREATE EXTENSION IF NOT EXISTS vector;'))
    conn.commit()

def init_db_and_tables():
    with engine.begin() as conn:
        SQLModel.metadata.create_all(conn)