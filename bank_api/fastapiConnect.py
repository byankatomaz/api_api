from fastapi import FastAPI, HTTPException, status
from api import url, url2, url3
from insertBank import popular_dados
from queryOne import find_Question
import requests

app = FastAPI()

@app.get('/questions')
async def get_quiz():

    response = requests.get(url3)
    data = response.json()

    for i in range(len(data['results'])):
        print('entrei')
        popular_dados(data['results'][i])
    
    return data


@app.get('/questions/{question_id}')
async def get_question(question_id: int):
    return find_Question(question_id)


# @app.post('/newQuestion')
# async def post_question():
    


if __name__ == '__main__':

    import uvicorn
    uvicorn.run("fastapiConnect:app", host='127.0.0.1', port=8000, reload=True)