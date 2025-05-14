from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from importlib import import_module

models = import_module("01_basic_model")

engine = create_engine("sqlite:///users.db")
Session = sessionmaker(bind=engine)
session = Session()

def get_user_by_email(email: str):
    user = session.query(models.User).filter_by(email=email).first()
    if user:
        return models.UserSchema.from_orm(user)
    return None

print(get_user_by_email("alice@example.com"))