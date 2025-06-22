from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
from package.utils.utils import now_utc

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .project import Project


class User(SQLModel, table=True):
    user_id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    password: str
    email: str
    created_dt: datetime = Field(default_factory=now_utc)
    updated_dt: datetime = Field(default_factory=now_utc)
    projects: List["Project"] = Relationship(
        back_populates="owner",
        sa_relationship_kwargs={"cascade": "all, delete"}
    )
