from models import User, Comment
from main import session

Byanka = User (
    username = "Byanka",
    email_address = "byankatomaz@gmail.com",
    comments = [
        Comment(text="Hello word"),
        Comment(text="OMAGA")
    ]
)

paul =  User (
    username = "paul",
    email_address = "paul@gmail.com",
    comments = [
        Comment(text="Hello, i'am paul"),
        Comment(text="I have 21 old years")
    ]
)

cathy = User (
    username = "cathy",
    email_address = "cathy@gmail.com",
)

session.add_all([Byanka, paul, cathy])

session.commit()