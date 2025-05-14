from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import StaleDataError

Base = declarative_base()

# Define the Product class with a version column for optimistic locking
class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    version = Column(Integer, default=1)

# Connect to the database
engine = create_engine('sqlite:///example.db')

# Create the table (if it doesn't exist)
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Insert a product to test
def insert_product(product_id, name, price):
    new_product = Product(id=product_id, name=name, price=price)
    session.add(new_product)
    session.commit()

# Update a product with optimistic locking
def update_product(product_id, new_name, new_price):
    product = session.query(Product).filter_by(id=product_id).first()
    if not product:
        print(f"Product {product_id} not found.")
        return

    # Simulate the version check for concurrency control
    try:
        product.name = new_name
        product.price = new_price
        product.version += 1  # Increment the version number

        session.commit()
        print(f"Product {product_id} updated successfully.")
    except StaleDataError:
        print(f"Error: Product {product_id} has been modified by another user. Please retry.")

# Example Usage
insert_product(1, "Product A", 29.99)

# Simulating two concurrent updates:
# First update attempt (Simulating version conflict)
update_product(1, "Updated Product A", 39.99)

# Second update attempt (Concurrency conflict simulated)
update_product(1, "Another Update", 49.99)
