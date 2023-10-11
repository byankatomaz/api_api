from main import session
from models import Questions


# Aqui é uma função onde faz uma query no banco para buscar todas as questões do banco e retorna isso
def findAllQuestion():
    query = session.query(Questions).all()
    questions_with_answers = []
    #Faz um for em cada questão restornada
    for question in query:
        # Montar as respostas corretas e incorretas
        
        """Pega por meio da correct_answer:Mapped["Correct"] = relationship(back_populates='question', passive_deletes=True)
        pegando o nome da resposta correta question.correct_answer.correct_text"""
        correct_answers = question.correct_answer.correct_text
        
        """Pega por meio da incorrect_answer:Mapped[List["Incorrect"]] = relationship(back_populates='question', passive_deletes=True) 
        e faz um for para pegar todas as respostas incorretas"""
        incorrect_answers = [incorrect.incorrect_text for incorrect in question.incorrect_answer]
        
        #modelde de como vai ser retornada a resposta
        question_data = {
            "id": question.id,
            "question": question.question,
            "category": question.category,
            "difficult": question.difficult,
            "type_question": question.type_question,
            "correct_answers": correct_answers,
            "incorrect_answers": incorrect_answers,
        }
        questions_with_answers.append(question_data)

    return questions_with_answers
