from fastapi import FastAPI, HTTPException, status
from api import url, url2, url3
from models import InsertQuestion, Questions
from insertBank import insert_data_api, post_data
from queryOne import findOneQuestion
from queryAll import findAllQuestion
from editQuestion import edit_question
from deleting import deleteOneQuestion
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#Configurar o CORS (permitir acesso de qualquer origem)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://10.109.71.13:5173"],  # Substitua pela origem do seu aplicativo Vite
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/populating')
async def get_quiz():
    try:
        urls = [url, url2, url3]
        i = 0

        for i in range(len(urls)):
            response = requests.get(urls[i])
            data = response.json()

            for i in range(len(data['results'])):
                print('entrei')
                insert_data_api(data['results'][i])
            i+=1
        
        return data

    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Unable to populate the database')



@app.get('/')
async def get_main():
    try:
        return {"message": "Hello, welcome on my API."}
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Unable to access API')
    


@app.get('/questions')
async def get_question():
    try:
        return findAllQuestion()
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Unable to access the Questions')



@app.get('/questions/{question_id}')
async def get_question(question_id: int):
    try:
        question = findOneQuestion(question_id) 
        return question
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Sorry, question not found')



@app.post('/newQuestion')
async def post_question(questionNew: InsertQuestion):
    try:
        post_data(questionNew)
        raise HTTPException(status_code=status.HTTP_201_CREATED, detail='Congratulations, questions went insert with success!')
    except KeyError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Sorry, unable to create question')



@app.put('/editQuestion/{question_id}')
async def put_question(question_id: int, questionUpdate:InsertQuestion):
    try:
        questionUpdate.id = question_id
        edit_question(questionUpdate)

        raise HTTPException(status_code=status.HTTP_200_OK, detail='Congratulations, question was edited successfully!')
    except KeyError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Sorry, unable to edit question')



@app.delete('/delQuestion/{question_id}')
async def put_question(question_id: int):
    try:
        deleteOneQuestion(question_id)
        raise HTTPException(status_code=status.HTTP_200_OK, detail='Congratulations, question was delete successfully!')
    except KeyError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Sorry, unable to delte question')
    

if __name__ == '__main__':

    import uvicorn
    uvicorn.run("fastapiConnect:app", host='10.109.71.13', port=8000, reload=True)