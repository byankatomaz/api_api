from models import *
from main import session
from queryOne import findOneQuestion

def edit_question(questionEdit):
    questionUp = findOneQuestion(questionEdit.id)
    i = 0

    if questionUp:

        questionUp.question=questionEdit.question
        questionUp.category=questionEdit.category
        questionUp.difficult=questionEdit.difficult
        questionUp.type_question=questionEdit.type_question
        questionUp.correct_answer.correct_text = questionEdit.correct_answer
    
        for incorrect in questionUp.incorrect_answer:
            if i < len(questionEdit.incorrect_answer):
                incorrect.incorrect_text = questionEdit.incorrect_answer[i]
                i+=1
            else:
                break



    session.commit()

    return questionUp


