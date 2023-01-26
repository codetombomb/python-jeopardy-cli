#!/usr/bin/env python3
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    DateTime,
    Table,
    ForeignKey,
    Boolean,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine("sqlite:///jeopardy.db")

Base = declarative_base()

user_question = Table(
    "user_question",
    Base.metadata,
    Column("user_id", ForeignKey("users.id")),
    Column("question_id", ForeignKey("questions.id")),
)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key=True)
    username = Column(String(), nullable=False)

    questions = relationship(
        "Question", secondary=user_question, back_populates="users"
    )

    def __repr__(self):
        return f"<User id={self.id}, " + f"username={self.username}>"


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer(), primary_key=True)
    clue = Column(String(), nullable=False, unique=True)
    response = Column(String(), nullable=False)
    category = Column(String(), nullable=False)
    value = Column(Integer(), nullable=False)
    cb_game_id = Column(Integer(), nullable=False)
    daily_double = Column(Boolean(), default=False)
    game_round = Column(String(), nullable=False)

    users = relationship("User", secondary=user_question, back_populates="questions")

    def __repr__(self):
        return f"<Question id={self.id}, clue={self.clue}, response={self.response}, category={self.category}, value={self.value} >"
