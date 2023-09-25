from fastapi import FastAPI, HTTPException, status
import json
import requests
from random import randrange

app = FastAPI()

@app.get('/')
async def get_quiz():
    apiKey = 'dPPZ9lwtQQZcqH8sqKAob5kSRfB70UCJtUXvuLoo'

    url = 'https://quizapi.io/api/v1/questions'

    params = {
        'apiKey':apiKey,
        'limits': 10
    }

    response = requests.get(url,apiKey=apiKey, limits=10)
    
    data = response.json()
    return data


if __name__ == '__main__':

    import uvicorn
    uvicorn.run("teste:app", host='127.0.0.1', port=8000, reload=True)

