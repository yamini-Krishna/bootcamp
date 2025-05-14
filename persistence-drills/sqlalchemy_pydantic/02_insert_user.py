from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from pydantic import BaseModel, EmailStr
from importlib import import_module

models = import_module("01_basic_model")

engine = create_engine("sqlite:///users.db")
Session = sessionmaker(bind=engine)
session = Session()

class CreateUser(BaseModel):
    name: str
    email: EmailStr

user_data = CreateUser(name="Alice", email="alice@example.com")
new_user = models.User(**user_data.dict())
session.add(new_user)
session.commit()
print("User inserted")