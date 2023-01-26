import requests
from models import User, Question
from ipdb import set_trace
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Cluebase API: https://cluebase.readthedocs.io/en/latest/
# cb_base: cluebase.lukelav.in/
# Jservice API: https://jservice.io/api/categories?count=50

clues_resp = requests.get("http://cluebase.lukelav.in/clues?limit=900")

engine = create_engine("sqlite:///jeopardy.db")
Session = sessionmaker(bind=engine)
session = Session()

# CLEAR OUT DB
session.query(User).delete()
session.query(Question).delete()

tom = User(username="tom_tobar")
monica = User(username="monica_gerard")

session.add_all([tom, monica])
session.commit()

# ========CREATE QUESTIONS============
for clue in clues_resp.json()["data"]:
    new_clue = Question(
        clue=clue["clue"],
        response=clue["response"],
        category=clue["category"],
        value=clue["value"],
        cb_game_id=clue["game_id"],
        daily_double=clue["daily_double"],
        game_round=clue["round"],
    )
    
    session.add(new_clue) # CREATE THE SQL
    session.commit() 
    
# Associate 10 questions to each user
for n in range(1,11):
    q = session.query(Question).filter(Question.id == n).first()
    set_trace()
    tom.questions.append(q)
    session.add(tom)
    session.commit()
    
set_trace()
