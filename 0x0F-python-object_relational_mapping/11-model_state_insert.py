#!/usr/bin/python3
"""
Adds a new state object to the database.
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Extract the command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

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

    # Create, add and commit new state to database
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Display new state id
    print(f"{new_state.id}")

    # Close session
    session.close()
