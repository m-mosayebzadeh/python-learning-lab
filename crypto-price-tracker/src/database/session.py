from sqlalchemy.orm import sessionmaker
from database.config import engine

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_session():
    
    session = SessionLocal()
    
    try:
        yield session
    finally:
        session.close()