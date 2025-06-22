from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING
from package.utils.utils import now_utc, datetime

if TYPE_CHECKING:
    from .user import User

class Workspace(SQLModel, table=True):
    workspace_id: Optional[int] = Field(default=None, primary_key=True)
    workspace_name: str = Field(index=True, unique=False)
    owner_id: int = Field(foreign_key="user.user_id")
    created_dt: datetime = Field(default_factory=now_utc)
    updated_dt: datetime = Field(default_factory=now_utc)
    owner: Optional["User"] = Relationship(back_populates="workspaces")