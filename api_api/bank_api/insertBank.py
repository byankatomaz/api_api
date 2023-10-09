from models import Questions, Correct, Incorrect, InsertQuestion
from main import session

    
def insert_data_api(data):

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


def post_data(question_data):

    correct_answers = [Correct(correct_text=text) for text in question_data.correct_answer]
    incorrect_answers = [Incorrect(incorrect_text=text) for text in question_data.incorrect_answer]

    questions = Questions(
        question=question_data.question,
        category=question_data.category,
        difficult=question_data.difficult,
        type_question=question_data.type_question,
        correct_answer=correct_answers,
        incorrect_answer=incorrect_answers
    )


    session.add_all([questions])

    session.commit()

