from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import User, Question
from game_board import GameBoard

if __name__ == '__main__':
    engine = create_engine('sqlite:///jeopardy.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    first_30 = session.query(Question).filter(Question.id <= 30).all()
    game_board = GameBoard(first_30)
    
    import ipdb; ipdb.set_trace()
    
