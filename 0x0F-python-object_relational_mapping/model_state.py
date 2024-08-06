from sqlalchemy import create_engine
from sqlalchemy import Column , Integer , String 
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer,autoincrement=True, primary_key=True,nullable=False)
    name =Column(String(128),nullable=False)


if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://root:thisis1yearplan2025@localhost:3306/hbtn_0e_6_usa")
    Base.metadata.create_all(engine)
