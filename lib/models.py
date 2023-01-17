#!/usr/bin/env python3
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///jeopardy.db')

Base = declarative_base()

user_question = Table(
    "user_question",
    Base.metadata,
    Column("user_id", ForeignKey("users.id")),
    Column("question_id", ForeignKey("questions.id"))
)

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer(), primary_key=True)
    username = Column(String(), nullable=False)
    
    def __repr__(self):
        return f"<User id={self.id}, " + \
             f"username={self.username}>"
             
             
class Question(Base):
    __tablename__ = 'questions'
    
    id = Column(Integer(), primary_key=True)
    question = Column(String(), nullable=False, unique=True)
    answer = Column(String(), nullable=False)
    category = Column(String(), nullable=False)
    value = Column(Integer(), nullable=False)
    
    def __repr__(self):
        return f"<Question id={self.id}, question={self.question}, answer={self.answer}, category={self.category}, value={self.value} >"
    
             
           
           
           
#   create_table "questions", force: :cascade do |t|
#     t.text    "question"
#     t.string  "answer"
#     t.string  "category"
#     t.integer "category_id"
#     t.integer "value"
#   end

#   create_table "user_questions", force: :cascade do |t|
#     t.integer "user_id"
#     t.integer "question_id"
#   end

#   create_table "users", force: :cascade do |t|
#     t.string  "username"
#     t.string  "password"
#     t.integer "high_score", default: 0
#   end


# Game Model 
# 
    # "id": 37949,
    # "answer": "dividends",
    # "question": "Preferred stock holders receive these payouts of corporate earnings before common stock holders",
    # "value": 300,
    # "airdate": "1995-02-15T20:00:00.000Z",
    # "created_at": "2022-12-30T18:53:21.305Z",
    # "updated_at": "2022-12-30T18:53:21.305Z",
    # "category_id": 3098,
    # "game_id": 6725,
    # "invalid_count": null,
    # "category": {
    #   "id": 3098,
    #   "title": "finance",
    #   "created_at": "2022-12-30T18:53:21.179Z",
    #   "updated_at": "2022-12-30T18:53:21.179Z",
    #   "clues_count": 13

