#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Unpack command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create a database engine
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"
    )

    # Bind the engine to the Base metadata
    Base.metadata.create_all(engine)

    # Create a configured session class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query all states with letter 'a'
    states = session.query(State).filter(State.name.like('%a%')).all()

    # Delete each state found
    for state in states:
        session.delete(state)

    # Commit change
    session.commit()

    # Close session
    session.close()
