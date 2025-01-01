#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    # Extract command-line args
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"
    )

    # Bind the engine to the Base metadata
    Base.metadata.create_all(engine)

    # Create a Session class
    Session = sessionmaker(bind=engine)

    # Create session
    session = Session()

    # Fetch city and state by criteria
    results = (
        session.query(City, State)
        .join(State, City.state_id == State.id)
        .order_by(City.id)
        .all()
    )

    # Print result
    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close session
    session.close()
