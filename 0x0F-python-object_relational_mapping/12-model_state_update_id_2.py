#!/usr/bin/python3
"""
This script lists all State objects from the database hbtn_0e_6_usa and adds a new State object.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def main():
    # Check for correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: ./10-model_state_y_get.py <mysql username> <mysql password> <database name> <state name>")
        sys.exit(1)

    # Extract arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    new_state_name = 'New Mexico'
    state_id=2

    # Create an engine and session
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}', pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # updated a new State object
    
    # Query all State objects
    state_to_update = session.query(State).filter(State.id == state_id).one_or_none()
    states = session.query(State).order_by(State.id).all()

    session.commit()
    state_to_update.name = new_state_name
    # Display the results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()

if __name__ == "__main__":
    main()
