import pandas as pd
from db.models import Movie, User, Rating
from db.database import SessionLocal, init_db

def load_data():
    init_db()
    session = SessionLocal()

    # Movies
    movies = pd.read_csv("data/movies.csv")
    for _, row in movies.iterrows():
        movie = Movie(movieId=row["movieId"], title=row["title"], genres=row["genres"])
        session.merge(movie)  # Avoid duplicate

    # Ratings
    ratings = pd.read_csv("data/ratings.csv")
    user_ids = ratings["userId"].unique()
    for user_id in user_ids:
        session.merge(User(userId=int(user_id)))

    for _, row in ratings.iterrows():
        rating = Rating(
            userId=int(row["userId"]),
            movieId=int(row["movieId"]),
            rating=float(row["rating"]),
            timestamp=int(row["timestamp"])
        )
        session.add(rating)

    session.commit()
    session.close()

if __name__ == "__main__":
    load_data()
