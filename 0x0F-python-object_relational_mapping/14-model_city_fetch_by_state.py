#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

def main():
    if len(sys.argv) != 4:
        print("Usage: 14-model_city_fetch_by_state.py <mysql username> <mysql password> <database name>")
        return

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create the engine and connect to the database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')
    Base.metadata.create_all(engine)

    # Create a configured "Session" class and a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database
    results = session.query(City, State).join(State).order_by(City.id).all()

    # Print the results
    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()

if __name__ == "__main__":
    main()
