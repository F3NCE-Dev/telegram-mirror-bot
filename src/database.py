from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///bot_branches.db"

engine = create_engine(
    url=DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=True,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Branch(Base):
    __tablename__ = "branches"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, index=True)
    branch_name = Column(String)
    input_id = Column(Integer)
    output_id = Column(Integer)

Base.metadata.create_all(bind=engine)
