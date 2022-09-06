import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__='user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), unique = True, nullable=False)
    first_name = Column(String(250), unique = False)
    last_name = Column(String(250), unique = False)
    email = Column(String(250), unique = True, nullable = False)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key= True)
    name = Column(String(250), unique = True, nullable = False)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key= True)
    name = Column(String(250), unique = True, nullable = False)

class UserPlanetFavorite(Base):
    __tablename__ = 'user_planet_favorite'
    user_id = Column(Integer, ForeignKey("user.id"), primary_key = True)
    planet_id = Column(Integer, ForeignKey("planet.id"), primary_key = True)

class UserCharacterFavorite(Base):
    __tablename__ = 'user_character_favorite'
    user_id = Column(Integer, ForeignKey("user.id"), primary_key = True)
    character_id = Column(Integer, ForeignKey("character.id"), primary_key = True)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')