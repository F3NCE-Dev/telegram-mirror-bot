from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from datetime import datetime

from config import settings

engine = create_engine(
    url=settings.DATABASE_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Branch(Base):
    __tablename__ = "branches"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, index=True)
    branch_name = Column(String, nullable=False)
    input_id = Column(Integer, nullable=False)
    output_id = Column(Integer, nullable=False)
    status = Column(Boolean, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class BeyondMessage(Base):
    __tablename__ = "Beyond Message"

    user_id = Column(Integer, primary_key=True, index=True)
    addition = Column(String)

def init_db():
    Base.metadata.create_all(bind=engine)
