from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime, timezone
from typing import Optional, List

def now_utc():
    return datetime.now(timezone.utc)

class Workspace(SQLModel, table=True):
    workspace_id: Optional[int] = Field(default=None, primary_key=True)
    workspace_name: str = Field(index=True, unique=False)
    owner_id: int = Field(foreign_key="user.user_id")
    created_dt: datetime = Field(default_factory=now_utc)
    updated_dt: datetime = Field(default_factory=now_utc)
    owner: Optional["User"] = Relationship(back_populates="workspaces")

class User(SQLModel, table=True):
    user_id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    password: str
    email: str
    created_dt: datetime = Field(default_factory=now_utc)
    updated_dt: datetime = Field(default_factory=now_utc)
    workspaces: List[Workspace] = Relationship(
            back_populates="owner",
            sa_relationship_kwargs={"cascade": "all, delete"}
        )
