import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from settings import MYSQL_USERNAME, MYSQL_DATABASE, MYSQL_PASSWD, MYSQL_HOST

DB_URL = f"mysql+mysqlconnector://{MYSQL_USERNAME}:{MYSQL_PASSWD}@{MYSQL_HOST}:3306/{MYSQL_DATABASE}"

engine = create_engine(DB_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
