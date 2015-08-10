from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base): 

	__tablename__ = 'user'
 	id = Column(Integer, primary_key=True)
	name = Column(String)
	email = Column(String)
	password = Column(String)


class StatusC(Base): 

	__tablename__ = 'statusC'
 	id = Column(Integer, primary_key=True)
	status= Column(String)
	likes= Column(Integer)
	dop= Column(String)
	user_posted= Column(Integer)

class StatusB(Base): 

	__tablename__ = 'statusB'
 	id = Column(Integer, primary_key=True)
	status= Column(String)
	likes= Column(Integer)
	dop= Column(Date)
	user_posted= Column(Integer)


