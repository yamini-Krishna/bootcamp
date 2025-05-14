from sqlalchemy import Column, Integer, String, DateTime, create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///users.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# ---------------- Schema-First ----------------
# Used when tables already exist, map them with reflection
# Not shown here since it requires a pre-existing DB

# ---------------- Code-First ----------------
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(DateTime)

# Generate schema from model
Base.metadata.create_all(engine)
