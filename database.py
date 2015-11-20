from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://postgres@localhost:5432/tf-tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
