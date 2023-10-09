from sqlalchemy import update
from models import *
from main import session
from queryOne import findOneQuestion

    
# def edit_question():
    
    # questionUp = findOneQuestion(questionEdit.id)
    
    # correct_answers = [Correct(idQuestion=questionEdit.id, correct_text=text) for text in questionEdit.correct_answer]
        # incorrect_answers = [Incorrect(idQuestion=questionEdit.id, incorrect_text=text) for text in questionEdit.incorrect_answer]
        
        
        # Atualize os campos da pergunta

    # correct_answers = [Correct(correct_text=text) for text in questionEdit.correct_answer]
    # incorrect_answers = [Incorrect(incorrect_text=text) for text in questionEdit.incorrect_answer]

    # questionUp.question=questionEdit.question,
    # questionUp.category=questionEdit.category,
    # questionUp.difficult=questionEdit.difficult,
    # questionUp.type_question=questionEdit.type_question,
    # questionUp.correct_answer=correct_answers,
    # questionUp.incorrect_answer=incorrect_answers

    # session.commit()
    
     # Encontre a pergunta existente pelo ID
    # Encontre a pergunta existente pelo ID

    
    # correct_answer = ["EU ATUALIZEI"]
    # incorrect_answer = ["eu atualizei", "eu atualizei", "eu atualizei"]
    

    # if questionUp:
    #     # Atualize os campos da pergunta
    #     questionUp.question = "eu atualizei1"
    #     questionUp.category = "eu atualizei1"
    #     questionUp.difficult = "eu atualizei1"
    #     questionUp.type_question = "eu atualizei1"
        
    #     # Atualize as respostas corretas
    #     correct_answer = ["EU ATUALIZEI"]
    #     questionUp.correct_answer = [
    #         Correct(id=6, idQuestion=questionUp.id, correct_text=text)
    #         for text in correct_answer
    #     ]

    #     # Atualize as respostas incorretas
    #     incorrect_answer = ["eu atualizei", "eu atualizei", "eu atualizei"]
    #     questionUp.incorrect_answer = [
    #         Incorrect(id=6, idQuestion=questionUp.id, incorrect_text=text)
    #         for text in incorrect_answer
    #     ]

    #     # Commit a transação
    #     session.commit()
    
#     questionUp = findOneQuestion(3)
#     query = (
#         update(Questions)
#         .where(Questions.id == questionUp.id)
#         .where(Correct.idQuestion == Questions.id)
#         .where(Incorrect.idQuestion == Questions.id)
#         .values(
#             {
#                 Questions.question: "eu atualizei21",
#                 Questions.category: "eu atualizei2",
#                 Questions.difficult: "eu atualizei2",
#                 Questions.type_question: "eu atualizei2",
#                 Correct.correct_text: ["olajurwvam"],
#                 Incorrect.incorrect_text: ["olajurwvam", "a", "b"],
#             }
            
            
#         )
#     )
    
#     session.commit()

# edit_question()

def edit_question(questionEdit):
    # Encontre a pergunta pelo ID
    questionUp = findOneQuestion(questionEdit.id)

    if questionUp:
        # Atualize os campos da pergunta
        questionUp.question=questionEdit.question
        questionUp.category=questionEdit.category
        questionUp.difficult=questionEdit.difficult
        questionUp.type_question=questionEdit.type_question

        # # Atualize as respostas corretas
        # correct_answer_text = ["siiiiiiiim"]
        for correct in questionUp.correct_answer:
            correct.correct_text = questionEdit.incorrect_answer[0]

        # Atualize as respostas incorretas
        # incorrect_answer_text = ["olajurwvam", "a", "b"]
        for incorrect in questionUp.incorrect_answer:
            incorrect.incorrect_text = questionEdit.incorrect_answer.pop(0)

        # Commit a transação
        session.commit()



