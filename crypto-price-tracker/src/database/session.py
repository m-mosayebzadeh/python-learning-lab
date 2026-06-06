from sqlalchemy.orm import sessionmaker
from config import engine

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_local_session():
    
    session = SessionLocal()
    
    try:
        yield session
    finally:
        session.close()