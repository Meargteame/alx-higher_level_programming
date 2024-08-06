#!/usr/bin/python3
"""
This module defines a State class and connects to a MySQL database.
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

# Create an instance of the declarative base
Base = declarative_base()

class State(Base):
    """
    Represents a state in the MySQL database.
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    # Create an engine that connects to the MySQL server
    engine = create_engine('mysql+mysqldb://root:thisis1yearplan2025@localhost:3306/hbtn_0e_6_usa', pool_pre_ping=True)
    
    # Create the table in the database
    Base.metadata.create_all(engine)
