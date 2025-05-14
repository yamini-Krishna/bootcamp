import random
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///large_dataset.db", echo=False)
Session = sessionmaker(bind=engine)
session = Session()

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    created_at = Column(DateTime)

Base.metadata.create_all(engine)

def generate_large_dataset():
    # Naive approach (slow)
    for _ in range(1000000):
        product = Product(
            name=f"Product {random.randint(1, 100000)}",
            price=random.random() * 100,
            created_at=datetime.utcnow()
        )
        session.add(product)
    session.commit()

def batch_insert_large_dataset():
    # Efficient batch insert
    records = [
        Product(name="Product", price=random.random() * 100, created_at=datetime.utcnow())
        for _ in range(1000000)
    ]
    session.bulk_save_objects(records)
    session.commit()
