from sqlalchemy.orm import session
from . import models

def create_user(db:session,name: str,email:str):
    user= models.User(name= name,email= email)
    db.add(user)
    db.commit()
    db.refresh()
    return user

def get_user(db:session):
    return db.query(models.user).all
