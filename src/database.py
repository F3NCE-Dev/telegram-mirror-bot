from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///bot_users.db"

engine = create_engine(
    url=DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=True,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Appointment(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    branch_name = Column(String, nullable=False)
    input_id = Column(String, nullable=False)
    output_id = Column(String, nullable=False)

Base.metadata.create_all(bind=engine)
