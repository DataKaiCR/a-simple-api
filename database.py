from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# CONSTANT
SQLALCHEMY_DB = 'sqlite:///./db.sqlite'

engine = create_engine(SQLALCHEMY_DB, connect_args={'check_same_thread':False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()