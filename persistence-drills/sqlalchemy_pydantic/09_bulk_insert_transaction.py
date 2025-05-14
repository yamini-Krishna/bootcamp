from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from importlib import import_module

models = import_module("01_basic_model")
engine = create_engine("sqlite:///users.db")
Session = sessionmaker(bind=engine)
session = Session()

try:
    users = [
        models.User(name="Bob", email="bob@example.com"),
        models.User(name="Charlie", email="charlie@example.com")
    ]
    session.add_all(users)
    session.commit()
    print("Bulk insert successful")
except Exception as e:
    session.rollback()
    print("Insert failed", str(e))