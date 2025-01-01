#!/usr/bin/pyython3
"""
Contains the class definition of a city
"""


from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    """
    Definition of a city in the database

    Attributes:
        id (int): the city's id (primary key)
        name (str): The city's name.
        state_id (int): The id of the state the city belongs
    """
    __tablename__ = 'cities'

    id = Column(
        Integer, primary_key=True, autoincrement=True, nullable=False
    )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state_id'), nullable=False)
