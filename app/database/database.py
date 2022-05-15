
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String


Base = declarative_base()



class Rooms(Base):
    """This is the Room Table class that inherits from Base.
    It specifies the table name and columns of the database table."""

    __tablename__ = 'rooms'
    room_name = Column(String)    
    room_type = Column(String)


class People(Base):
    """This is the People Table class that inherits from Base.
    It specifies the table name and columns of the database table."""

    __tablename__ = 'people'
    first_name = Column(String)
    last_name = Column(String)
    person_type = Column(String)
    wants_accommodation = Column(String)