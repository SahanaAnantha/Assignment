from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *

Base = declarative_base()


# theatre movies model
class TheatreMovies(Base):
    __tablename__ = "theatre_movies"
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    releaseYear = Column(String(255))
    genres = Column(String(255))
    description = Column(String(255))
    theatre = Column(String(255))


# tv movies model
class TvMovies(Base):
    __tablename__ = "tv_movies"
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    releaseYear = Column(String(255))
    genres = Column(String(255))
    description = Column(String(255))
    channel_no = Column(String(255))
