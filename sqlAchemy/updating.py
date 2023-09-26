from main import session
from models import User, Comment
from sqlalchemy import select


comment =session.query(Comment).filter_by(id=1).first()

comment.text = "This is a update"

session.commit()