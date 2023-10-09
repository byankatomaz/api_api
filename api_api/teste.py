from fastapi import FastAPI, HTTPException, status
import json
import requests
from random import randrange

app = FastAPI()

@app.get('/')
async def get_quiz():

    url ='https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=multiple'
    
    response = requests.get(url)
    
    data = response.json()
    
    jurema = json.dumps(data, indent=4)
    
    print(jurema)
    
    return data


if __name__ == '__main__':

    import uvicorn
    uvicorn.run("teste:app", host='127.0.0.1', port=8000, reload=True)