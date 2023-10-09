from main import session
from models import User, Comment
from sqlalchemy import select

statement = select(Comment).join(Comment.user).where(
    User.username == 'Byanka'
).where(
    Comment.text == 'OMAGA'
)

result = session.scalars(statement).one()

print(result)