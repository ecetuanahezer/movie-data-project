## Movie Recommendation System
This project implements a movie recommendation system using the MovieLens dataset.
It demonstrates end-to-end data processing, exploratory analysis, and building recommendation models — from simple collaborative filtering to deep learning with TensorFlow.

### Tech Stack
Python: Data processing, analysis, and modeling

### Libraries:

- Data: pandas, numpy

- Database & Models: SQLAlchemy, Pydantic

- Visualization: matplotlib, seaborn

- Machine Learning: scikit-learn, TensorFlow

- Environment: Jupyter Notebook

### Workflow
#### 1. Data Loading & Processing
Loaded MovieLens data (movies.csv, ratings.csv) from CSV files

Used SQLAlchemy ORM to store and query data from a local database

Defined Pydantic models for data validation and schema clarity

#### 2. Exploratory Data Analysis (EDA)
Rating distributions (overall and per user)

Year-based trends in movie production and ratings

Popularity vs. rating analysis for movies

#### 3. User Behavior Analysis
Most active users

Users’ average ratings

Genre-based user preferences

#### 4. Recommendation Models
- Approach 1 – KNN Collaborative Filtering
Implemented a K-Nearest Neighbors recommender using scikit-learn

Finds similar movies based on user rating patterns

- Approach 2 – Deep Learning (TensorFlow)
Built a Neural Collaborative Filtering model with:

User embeddings

Movie embeddings

Dense layers to capture non-linear patterns

Trained and evaluated the model for recommendation accuracy

#### Results
KNN provides interpretable, similarity-based recommendations

TensorFlow model captures more complex user-movie interactions and can scale better for large datasets

### Files
- analysis.ipynb – Jupyter Notebook containing all steps

- movies.csv, ratings.csv – MovieLens dataset files
