from db import Base
from sqlalchemy import Column, String, Text, Integer

class User(Base):
    __tablename__ = "user_data"
    id = Column(Integer, primary_key = True, index = True, unique = True)
    name = Column(String)
    surname = Column(String)
    thirdname = Column(String)
    phone = Column(String, unique = True)
    review = Column(Text)