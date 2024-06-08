from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



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
    user_id = Column(Integer, nullable=True)
    card_price = Column(Integer, nullable=True)
    price = Column(Integer, nullable=True)
    photo = Column(Text, nullable=True)
    
def add(art, user, price_w, oz_price, photo):
    Session = sessionmaker()
    session = Session(bind=engine) 
    new = Articles(article = art, user_id = user, price = price_w, card_price = oz_price, photo = photo)
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

def my_articles(user):
    res = []
    Session = sessionmaker()
    session = Session(bind=engine)
    all = session.query(Articles).filter(Articles.user_id == user).all()
    session.close()
    for i in all:
        res.append(i.article)
    return res

def del_art(article, user):
    Session = sessionmaker()
    session = Session(bind=engine)
    session.query(Articles).filter(Articles.user_id == user, Articles.article == article).delete()
    session.commit()
    session.close()
    

Base.metadata.create_all(engine)
