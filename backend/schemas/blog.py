from datetime import datetime
from typing import Optional

from pydantic import BaseModel, model_validator


class CreateBlog(BaseModel):
    title: str
    slug: str
    content: Optional[str] = None

    @model_validator(mode="after")
    def generate_slug(cls, values):
        if "title" in values:
            values["slug"] = values.get("title").replace(" ", "-").lower()
        return values


class ShowBlog(BaseModel):
    title: str
    content: Optional[str] = None
    created_at: datetime

    class Config:
        orm_mode = True
