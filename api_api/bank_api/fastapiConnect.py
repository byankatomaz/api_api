from fastapi import FastAPI, HTTPException, status
from api import url, url2, url3
from models import InsertQuestion, Questions
from insertBank import insert_data_api, post_data
from queryOne import findOneQuestion
from queryAll import findAllQuestion
from editQuestion import edit_question
import requests

app = FastAPI()

@app.get('/populando')
async def get_quiz():

    response = requests.get(url3)
    data = response.json()

    for i in range(len(data['results'])):
        print('entrei')
        insert_data_api(data['results'][i])
    
    return data


@app.get('/')
async def get_main():
    return {"message": "Hello, welcome on my API."}
    

@app.get('/questions')
async def get_question():
    return findAllQuestion()


@app.get('/questions/{question_id}')
async def get_question(question_id: int):
    
    question = findOneQuestion(question_id) 
    
    if question:
        return question
    else:
        return {"message": "Sorry, question not found."}


@app.post('/newQuestion')
async def post_question(questionNew: InsertQuestion):
    post_data(questionNew)
    return {"message": "Congratulations, questions went insert with success!"}


@app.put('/editQuestion/{question_id}')
async def put_question(question_id: int, questionUpdate:InsertQuestion) -> dict:
    
    questionUpdate.id = question_id
    questionEdited = edit_question(questionUpdate)
    
    if questionEdited:
        return questionEdited
    else:
        return {"message": "Pergunta não encontrada"}
    
    


if __name__ == '__main__':

    import uvicorn
    uvicorn.run("fastapiConnect:app", host='127.0.0.1', port=8000, reload=True)