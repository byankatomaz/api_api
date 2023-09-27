from models import Questions, Correct, Incorrect
from main import session

    
def popular_dados(data):
    

    questions = Questions (
        question = data['question'],
        category = data['category'],
        difficult = data['difficulty'],
        type_question = data['type'],
        correct_answer = [
            Correct(correct_text=data['correct_answer']),
        ],
        incorrect_answer = [
            Incorrect(incorrect_text=data['incorrect_answers'][0]),
            Incorrect(incorrect_text=data['incorrect_answers'][1]),
            Incorrect(incorrect_text=data['incorrect_answers'][2])
        ]
    )


    session.add_all([questions])

    session.commit()

