from environs import Env
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

env = Env()
env.read_env(".env")
user = env.str("DB_USER")
passw = env.str("DB_PASSWORD")
host = env.str("DB_HOST")
name = env.str("DB_NAME")


DATABASE_URL = f"sqlite:///db.sqlite3"

# Создание объекта Engine
engine = create_engine(DATABASE_URL)

# Создание базового класса для моделей
Base = declarative_base()

# Определение модели User
class Articles(Base):
    __tablename__ = 'articles'
    id = Column(Integer, autoincrement=True, primary_key=True)
    article = Column(Integer, nullable=False)
    photo = Column(Text, nullable=True)
    user_id = Column(Integer, nullable=True)
    card_price = Column(Integer, nullable=True)
    price = Column(Integer, nullable=True)

def add(art, img, user, price_w, oz_price):
    Session = sessionmaker()
    session = Session(bind=engine) 
    new = Articles(article = art, photo = img, user_id = user, price = price_w, card_price = oz_price)
    session.add(new)
    session.commit()
    session.close()

def check(art: int, id: int):
    Session = sessionmaker()
    session = Session(bind=engine) 
    curr = session.query(Articles).filter(Articles.user_id == id, Articles.article == art).first()
    session.close()
    if curr is None:
        return True
    return False
    
def fetchall():
    Session = sessionmaker()
    session = Session(bind=engine) 
    res = session.query(Articles).all()
    session.close()
    return res

def change_price(price_card, price, art, user_id):
    Session = sessionmaker()
    session = Session(bind=engine)
    curr = session.query(Articles).filter(Articles.user_id == user_id, Articles.article == art).first()
    curr.card_price = price_card
    curr.price = price
    session.commit()
    session.close()



def de():
    Session = sessionmaker()
    session = Session(bind=engine) 
    res = session.query(Articles).all()
    for i in res:
        i.card_price = 123
        session.commit()
    session.close()

Base.metadata.create_all(engine)
de()