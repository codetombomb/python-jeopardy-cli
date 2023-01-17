#!/usr/bin/env python3
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///jeopardy.db')

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer(), primary_key=True)
    username = Column(String(), nullable=False)
    
    def __repr__(self):
        return f"<User id={self.id}, " + \
             f"username={self.username}>"

