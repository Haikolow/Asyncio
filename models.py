import os
from sqlalchemy import Column, Integer, JSON, String
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

PG_USER = os.getenv('PG_USER', 'test')
PG_PASSWORD = os.getenv('PG_PASSWORD', 'test')
PG_DB = os.getenv('PG_DB', 'Asyncio_db')
PG_HOST = os.getenv('PG_HOST', '127.0.0.1')
PG_PORT = os.getenv('PG_PORT', '5431')

PG_DSN = f"postgresql+asyncpg://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}"

engine = create_async_engine(PG_DSN)
Session = sessionmaker(class_=AsyncSession, expire_on_commit=False, bind=engine)

Base = declarative_base()


class SwapiPeople(Base):
    __tablename__ = 'swapi_people'

    id = Column(Integer, primary_key=True)
    birth_year = Column(String)
    eye_color = Column(String)
    films = Column(String)
    gender = Column(String)
    hair_color = Column(String)
    height = Column(String)
    homeworld = Column(String)
    mass = Column(String)
    name = Column(String)
    skin_color = Column(String)
    species = Column(String)
    starships = Column(String)
    vehicles = Column(String)