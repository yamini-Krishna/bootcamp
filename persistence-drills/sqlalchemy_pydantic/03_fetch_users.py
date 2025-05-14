from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from importlib import import_module

models = import_module("01_basic_model")

engine = create_engine("sqlite:///users.db")
Session = sessionmaker(bind=engine)
session = Session()

users = session.query(models.User).all()
user_schemas = [models.UserSchema.from_orm(user) for user in users]
print(user_schemas)