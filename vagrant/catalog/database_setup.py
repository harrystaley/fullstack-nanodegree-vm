import sys

from sqlalchemy import
Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import
declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

base = declarative_base()
# end beginning config code
# place class defs between this and the end config code

# class defitions


class Restraunt(base):
    __tablename__ = 'restraunt'
    name = Column(
        string(80), nullable=False)
    id = Collumn(
        Integer, Primary_Key=True)


class MenuItem(base):
    __tablename__ = 'menu_item'
    name = Column(
        string(80), nullable=False)
    id = Collumn(
        Integer, Primary_Key=True)
    course = Collumn(
        string(250))
    description = Collumn(
        string(250))
    price = Collumn(
        string(8))
    restraunt_id = Collumn(
        integer, ForeignKey('restraunt.id'))
    restraunt = relationship(Restraunt)


# begin end config code
engine = create_engine('sqlite:///restrauntmenu.db')
base.metadata.create_all(engine)
