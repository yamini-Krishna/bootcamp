from sqlalchemy import Column, Integer, String, DateTime, create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta

Base = declarative_base()
engine = create_engine("sqlite:///products.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    deleted_at = Column(DateTime, nullable=True)

Base.metadata.create_all(engine)

def soft_delete_product(product_id):
    session.execute(
        text("UPDATE products SET deleted_at = CURRENT_TIMESTAMP WHERE id = :id"),
        {"id": product_id}
    )
    session.commit()

def cleanup_deleted_products():
    session.execute(
        text("DELETE FROM products WHERE deleted_at < datetime('now', '-30 days')")
    )
    session.commit()
