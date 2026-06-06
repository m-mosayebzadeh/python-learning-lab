from sqlalchemy import create_engine

SQLLITE_DB_URL = "sqlite:///./app.db"

engine = create_engine(
    SQLLITE_DB_URL,
    connect_args={"check_same_thread": False} ## فقط برای SQLLITE مهمه
)
