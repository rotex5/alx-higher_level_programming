#!/usr/bin/python3
"""
contains the class definition of a City
and an instance Base = declarative_base()
"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    Class representation of a city
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("state.id"), nullable=False)
