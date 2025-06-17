from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base, engine
from sqlalchemy.orm import relationship

def create_tables():
    Base.metadata.create_all(engine)



class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True, index = True)
    username = Column(String, unique = True, index = True)
    email = Column(String, unique = True, index = True)
    password = Column(String)



class Blog(Base):
    __tablename__ = "blogs"
    id = Column(String, primary_key = True, index = True)
    title = Column(String)
    content = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    creater = relationship("User", back_populates="blogs")

    





