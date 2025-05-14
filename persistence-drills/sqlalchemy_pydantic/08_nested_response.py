from pydantic import BaseModel
from typing import List

class PostSchema(BaseModel):
    id: int
    title: str
    content: str

    model_config = {
        'from_attributes': True
    }

class UserSchema(BaseModel):
    id: int
    name: str
    email: str
    posts: list[PostSchema] = []

    model_config = {
        'from_attributes': True
    }

