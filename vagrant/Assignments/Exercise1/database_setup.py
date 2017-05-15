import os
import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric

Base = declarative_base()

class Shelter(Base):

	__tablename__ = 'shelter'

	name = Column(String(32), nullable = False)
	address = Column(String(250))
	city = Column(String(32))
	state = Column(String(32))
	zipCode = Column(String(32))
	website = Column(String(250))
	id = Column(Integer, primary_key = True)

class Puppy(Base):

	__tablename__ = 'puppy'

	name = Column(String(32), nullable = False)
	dateOfBirth = Column(Date, nullable = False)
	gender = Column(String(6), nullable = False)
	weight = Column(Numeric(20))
	shelter_id = Column(Integer, ForeignKey('shelter.id'))
	shelter = relationship(Shelter)
	id = Column(Integer, primary_key = True)


engine = create_engine('sqlite:///shelter.db')
Base.metadata.create_all(engine)