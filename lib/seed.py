from models import User, Question
import requests

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

category_resp = requests.get("https://jservice.io/api/categories?count=50")
# resp = requests.get("https://jservice.io/api/random?count=100")

engine = create_engine('sqlite:///jeopardy.db')
Session = sessionmaker(bind=engine)
session = Session()

session.query(User).delete()
session.query(Question).delete()

tom = User(username="tom_tobar")
monica = User(username="monica_gerard")

session.add_all([tom,monica])
session.commit()

# ========CREATE QUESTIONS============

for cat in category_resp.json():

    category_questions = requests.get(f"https://jservice.io/api/clues?category={cat['id']}")
    
    for question in category_questions.json():
        session.add(Question(question=question["question"], answer=question["answer"], value=question["value"], category=question["category"]["title"]))
        session.commit()
        
        import ipdb; ipdb.set_trace()
        

        
