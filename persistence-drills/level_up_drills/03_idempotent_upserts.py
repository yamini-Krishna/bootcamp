from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)

# Connect to the database
engine = create_engine('sqlite:///products.db')

# Create the table (if it doesn't exist)
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Now the table is created, and you can perform the upsert
def upsert_product(product_id, name, price):
    existing_product = session.query(Product).filter_by(id=product_id).first()
    if existing_product:
        existing_product.price = price  # Update the price if the product exists
    else:
        new_product = Product(id=product_id, name=name, price=price)  # Insert new product
        session.add(new_product)
    session.commit()

# Call the upsert function
upsert_product(1, 'Product A', 19.99)
