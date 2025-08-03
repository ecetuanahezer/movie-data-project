from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Movie(Base):
    __tablename__ = "movies"
    movieId = Column(Integer, primary_key=True)
    title = Column(String)
    genres = Column(String)

    ratings = relationship("Rating", back_populates="movie")

class User(Base):
    __tablename__ = "users"
    userId = Column(Integer, primary_key=True)

    ratings = relationship("Rating", back_populates="user")

class Rating(Base):
    __tablename__ = "ratings"
    id = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey("users.userId"))
    movieId = Column(Integer, ForeignKey("movies.movieId"))
    rating = Column(Float)
    timestamp = Column(Integer)

    user = relationship("User", back_populates="ratings")
    movie = relationship("Movie", back_populates="ratings")