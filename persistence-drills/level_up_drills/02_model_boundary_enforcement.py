from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String

Base = declarative_base()

# SQLAlchemy model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(String)

# Pydantic model
class UserProfile(BaseModel):
    id: int
    name: str
    created_at: str

    class Config:
        from_attributes = True  # for Pydantic v2 compatibility

# Example function to get user profile
def get_user_profile(user_id: int, session):
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        return UserProfile.from_orm(user)
    else:
        return None

# Create engine and session
engine = create_engine('sqlite:///database.db')  # Use your actual database URL
Session = sessionmaker(bind=engine)
session = Session()

# Create all tables in the database (this will create the 'users' table if it doesn't exist)
Base.metadata.create_all(engine)

# Add test data if no user exists
if not session.query(User).first():
    new_user = User(id=1, name="John Doe", created_at="2025-05-14")
    session.add(new_user)
    session.commit()

# Example usage
# Now try to fetch the user
user_profile = get_user_profile(1, session)
if user_profile:
    print(user_profile)
else:
    print("User not found.")