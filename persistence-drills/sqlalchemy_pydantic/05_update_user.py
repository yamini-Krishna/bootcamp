from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from importlib import import_module

models = import_module("01_basic_model")

engine = create_engine("sqlite:///users.db")
Session = sessionmaker(bind=engine)
session = Session()

def update_email(user_id: int, new_email: str):
    user = session.query(models.User).filter_by(id=user_id).first()
    if user:
        user.email = new_email
        session.commit()
        return True
    return False

print(update_email(1, "alice_new@example.com"))