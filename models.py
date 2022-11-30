from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    ForeignKey,
    MetaData,
    Table,
    null,
)

from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()


class StudentGroup(Base):
    __tablename__ = "student_group"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    start = Column(Date, nullable=False)
    end = Column(Date, nullable=True)


class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(70), nullable=False)
    email = Column(String(50), nullable=True)
    group = Column(Integer(), ForeignKey("student_group.id"))










