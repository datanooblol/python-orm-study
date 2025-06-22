from sqlmodel import SQLModel, Field
from sqlalchemy.dialects.postgresql import JSONB
from pgvector.sqlalchemy import Vector
from package.config.settings import settings
from typing import Any

class LongTerm(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    context: str
    embedding: Any = Field(sa_type=Vector(settings.VECTOR_SIZE))
    meta: dict = Field(sa_type=JSONB, default_factory=dict)