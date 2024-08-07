#!/usr/bin/python3
"""
This script deletes a State object from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def main():
    # Check for correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: ./10-model_state_delete.py <mysql username> <mysql password> <database name> <state id>")
        sys.exit(1)

    # Extract arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = State.name.like('%a%')

    # Create an engine and session
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}', pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Query the State object to delete
        state_to_delete = session.query(State).filter_by(state_name).all()
        
        
        # Delete the State object
        session.delete(state_to_delete)

        # Commit the changes
        session.commit()

    except Exception as e:
        session.rollback()
        print(f"Error occurred: {e}")

    finally:
        # Close the session
        session.close()

if __name__ == "__main__":
    main()
