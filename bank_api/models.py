from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Text, ForeignKey
from typing import List

class Base(DeclarativeBase):
    pass

class Questions(Base):
    __tablename__ = 'questions'
    id:Mapped[int] = mapped_column(primary_key=True)
    question:Mapped[str] = mapped_column(nullable=False)
    category:Mapped[str] = mapped_column(nullable=False)
    difficult:Mapped[str] = mapped_column(nullable=False)
    type_question:Mapped[str]
    correct_answer:Mapped[List["Correct"]] = relationship(back_populates='question')
    incorrect_answer:Mapped[List["Incorrect"]] = relationship(back_populates='question')
    
    def __repr__(self) -> str:
        return f'<User username={self.question}>'

class Correct(Base):
    __tablename__ = 'correct'
    id:Mapped[int] = mapped_column(primary_key=True)
    idQuestion:Mapped[int] = mapped_column(ForeignKey('questions.id'), nullable=False)
    correct_text:Mapped[str] = mapped_column(Text, nullable=False)
    question:Mapped["Questions"] =  relationship(back_populates='correct_answer')
    
    def __repr__(self) -> str:
        return f'<Correct answer text={self. correct_text} by {self.question.question}>'
    

class Incorrect(Base):
    __tablename__ = 'incorrect'
    id:Mapped[int] = mapped_column(primary_key=True)
    idQuestion:Mapped[int] = mapped_column(ForeignKey('questions.id'), nullable=False)
    incorrect_text:Mapped[str] = mapped_column(Text, nullable=False)
    question:Mapped["Questions"] =  relationship(back_populates='incorrect_answer')
    
    def __repr__(self) -> str:
        return f'<Comment teste={self.incorrect_text} by {self.question.question}>'