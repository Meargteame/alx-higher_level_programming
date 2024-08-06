import sqlalchemy 
from sqlalchemy import create_engine
from sqlalchemy import Column , Integer , String 
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql://root:thisis1yearplan2025@locahost:/hbtn_0e_6_usa")

Session = sessionmaker()
session = Session()

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer,autoincrement=True, primary_key=True,unique=True, nullable=False)
    name =Column(String(128),nullable=False)



Base.metadata.create_all(engine)
session.commit()