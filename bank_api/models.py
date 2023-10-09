from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Text, ForeignKey
from typing import List, Optional
from pydantic import BaseModel


# Class Base para poder fazer o models do SQLAlchemy
class Base(DeclarativeBase):
    pass


# Class Questions é o modelo da tabela das questões, onde esta fazendo um relacionamento com as tabelas Correct e Incorrect, que são as alternativas
class Questions(Base):
    __tablename__ = 'questions'
    id:Mapped[int] = mapped_column(primary_key=True)
    question:Mapped[str] = mapped_column(nullable=False)
    category:Mapped[str] = mapped_column(nullable=False)
    difficult:Mapped[str] = mapped_column(nullable=False)
    type_question:Mapped[str]
    correct_answer:Mapped["Correct"] = relationship(back_populates='question', passive_deletes=True)
    incorrect_answer:Mapped[List["Incorrect"]] = relationship(back_populates='question', passive_deletes=True)
    
    def __repr__(self) -> str:
        return f'<Question question text={self.question}>'


# Class Correct é a tabela de respostas corretas que tem relação com a tabela Questions, onde a resposta correta esta ligada com a FK de sua questão
class Correct(Base):
    __tablename__ = 'correct'
    id:Mapped[int] = mapped_column(primary_key=True)
    idQuestion:Mapped[int] = mapped_column(ForeignKey('questions.id'), nullable=False)
    correct_text:Mapped[str] = mapped_column(Text, nullable=False)
    question:Mapped["Questions"] =  relationship(back_populates='correct_answer')
    
    def __repr__(self) -> str:
        return f'<Correct answer text={self. correct_text} by {self.question.question}>'
    

# Class Incorrect é a tabela de respostas incorretas que tem relação com a tabela Questions, onde as 3 respostas incorretas esta ligada com a FK de sua questão
class Incorrect(Base):
    __tablename__ = 'incorrect'
    id:Mapped[int] = mapped_column(primary_key=True)
    idQuestion:Mapped[int] = mapped_column(ForeignKey('questions.id'), nullable=False)
    incorrect_text:Mapped[str] = mapped_column(Text, nullable=False)
    question:Mapped["Questions"] =  relationship(back_populates='incorrect_answer')
    
    def __repr__(self) -> str:
        return f'<Incorrect answer text={self.incorrect_text} by {self.question.question}>'


# Class InsertQuestion esta sendo feita com o BaseModel do Pydantic, para que possamos fazer a inserção de dados no banco atraves do POST da API
class InsertQuestion(BaseModel):
    id: Optional[int] = None
    question: Optional[str]
    category: Optional[str]
    difficult: Optional[str]
    type_question: Optional[str]
    correct_answer: Optional[str]
    incorrect_answer: List[str] = [] 