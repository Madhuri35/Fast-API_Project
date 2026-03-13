from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base


Base= declarative_base()

class User(Base):
    __table_name__= "Users"
    
    
    id = Column(Integer,primary_key)
    name = Column(String)
    email = Column(String)
    
    