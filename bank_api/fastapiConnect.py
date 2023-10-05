from fastapi import FastAPI, HTTPException, status
from api import url, url2, url3
from models import InsertQuestion
from insertBank import popular_dados
from queryOne import findOneQuestion
from queryAll import findAllQuestion
import requests

app = FastAPI()

@app.get('/populando')
async def get_quiz():

    response = requests.get(url3)
    data = response.json()

    for i in range(len(data['results'])):
        print('entrei')
        popular_dados(data['results'][i])
    
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
        return     {"message": "Sorry, question not found."}


@app.post('/newQuestion')
async def post_question(questionNew: InsertQuestion):
    return questionNew
    
    


if __name__ == '__main__':

    import uvicorn
    uvicorn.run("fastapiConnect:app", host='0.0.0.0', port=8000, reload=True)