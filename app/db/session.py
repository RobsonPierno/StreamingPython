from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config.settings import Settings

settings = Settings()

engine = create_engine(settings.postgresql_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()