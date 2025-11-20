"""
Database configuration and models for PostgreSQL
Logs all prediction requests and responses
"""

import os
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Get database URL from environment variable
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://mluser:mlpassword@localhost:5432/ml_predictions"
)

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class PredictionLog(Base):
    """
    Table to log all predictions made by the model
    Useful for monitoring, debugging, and model drift detection
    """
    __tablename__ = "prediction_logs"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    model_version = Column(String, index=True)
    input_features = Column(JSON)
    prediction = Column(Float)
    prediction_proba = Column(Float, nullable=True)
    latency_ms = Column(Float)
    request_id = Column(String, unique=True, index=True)


def init_db():
    """
    Initialize database tables
    Call this when starting the application
    """
    Base.metadata.create_all(bind=engine)


def get_db():
    """
    Dependency for FastAPI to get database session
    Yields a database session and closes it after use
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
