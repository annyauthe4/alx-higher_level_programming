#!/usr/bin/python3
"""
Change the name of a state with id of 2.
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create database engine
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"
    )

    # Bind engine to Base metadata
    Base.metadata.create_all(engine)

    # Create configured session
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Get the state by id and update
    state = session.query(State).filter(State.id == 2).first()
    state.name = "New Mexico"
    session.commit()

    # Close session
    session.close()
