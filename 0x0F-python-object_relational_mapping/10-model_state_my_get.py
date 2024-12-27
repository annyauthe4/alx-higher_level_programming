#!/usr/bin/python3
"""
Prints the State object with the name passed as arg
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Extract command-line argument
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_searched = sys.argv[4]

    # Create database engine
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"
    )

    # Bind the engine to the Base metadata
    Base.metadata.create_all(engine)

    # Create a configured session class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query the state class by name
    state = session.query(State).filter(State.name == state_searched)\
        .first()

    # Display result
    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    # Close session
    session.close()
