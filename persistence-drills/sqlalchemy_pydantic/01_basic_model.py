from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

from pydantic import BaseModel

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)


class UserSchema(BaseModel):
    id: int
    name: str
    email: str

    model_config = {
        'from_attributes': True
    }


engine = create_engine("sqlite:///users.db")
Base.metadata.create_all(engine)