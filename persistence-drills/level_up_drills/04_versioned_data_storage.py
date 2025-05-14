from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Define the base for the declarative class
Base = declarative_base()

# Define the Product class
class Product(Base):
    __tablename__ = 'products'
    
    # Define the columns
    id = Column(Integer, primary_key=True, autoincrement=True)  # Auto-increment primary key
    name = Column(String)
    price = Column(Float)
    version = Column(Integer)
    created_at = Column(String)
    updated_at = Column(String)

# Create an SQLite engine
engine = create_engine('sqlite:///products1.db')

# Create the table in the database (if not already created)
Base.metadata.create_all(engine)

# Setup session
Session = sessionmaker(bind=engine)
session = Session()

# Insert product function with version control
def insert_product(product_id, product_name, product_price):
    # Check if the product with the given id exists
    existing_product = session.query(Product).filter_by(id=product_id).first()
    
    if existing_product:
        print(f"Product with id {product_id} already exists.")
    else:
        # Insert new product with version 1
        new_product = Product(
            id=product_id,
            name=product_name,
            price=product_price,
            version=1,
            created_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            updated_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )
        
        # Add and commit the new product
        session.add(new_product)
        session.commit()
        print(f"Inserted {product_name} with id {product_id}.")

# Example usage
insert_product(1, "Product A", 19.99)
insert_product(2, "Product B", 29.99)

# Example of updating product version (as a new version)
def update_product_version(product_id, new_name=None, new_price=None):
    product = session.query(Product).filter_by(id=product_id).first()
    
    if product:
        # Increment the version
        product.version += 1
        if new_name:
            product.name = new_name
        if new_price:
            product.price = new_price
        
        product.updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        session.commit()
        print(f"Updated product with id {product_id}. New version: {product.version}.")
    else:
        print(f"Product with id {product_id} not found.")

# Update a product
update_product_version(1, new_name="Product A Updated", new_price=21.99)

# Close the session
session.close()
