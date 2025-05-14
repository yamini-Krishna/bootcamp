from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from importlib import import_module

models = import_module("01_basic_model")

engine = create_engine("sqlite:///users.db")
Session = sessionmaker(bind=engine)
session = Session()

def delete_user(user_id: int):
    user = session.query(models.User).filter_by(id=user_id).first()
    if user:
        session.delete(user)
        session.commit()
        return True
    return False

print(delete_user(1))