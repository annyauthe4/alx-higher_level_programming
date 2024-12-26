#!/usr/bin/python3
"""
The class definition of a State and an instance Base = declarative_base():
The State class: inherits from Base, links to the MySQL table states
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


# Base instance for ORM
Base = declarative_base()


class State(Base):
    """
    State class:
    - Links to the MySQL table 'states'
    - id: Auto-generated, unisque integer primary key
    - name: String (max 128 chars), not null
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
