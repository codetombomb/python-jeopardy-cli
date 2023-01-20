from models import User, Question
import requests
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
    
    session.add(new_clue)
    session.commit()
    
    # nc = Question()
    # id = Column(Integer(), primary_key=True)
    # clue = Column(String(), nullable=False, unique=True)
    # response = Column(String(), nullable=False)
    # category = Column(String(), nullable=False)
    # value = Column(Integer(), nullable=False)
    # cb_game_id = Column(Integer(), nullable=False)
    # daily_double = Column(Boolean(), default=False)
    # game_round = Column(String(), nullable=False)
set_trace()
