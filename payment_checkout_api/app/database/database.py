import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:root@localhost:3307/test"

# docker run -d -p 3307:3306 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=test -e MYSQL_USER=MainUser -e MYSQL_PASSWORD=MainPassword mysql:5.7


SQLALCHEMY_DATABASE_URL = os.getenv(
    "SQLALCHEMY_DATABASE_URL", "sqlite:///./test.db")
#SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:root@db:3306/test"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
