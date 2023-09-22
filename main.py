from fastapi import FastAPI, HTTPException, status
import json
import requests

app = FastAPI()

message = {},{'slip': 
        {
            'id': 78, 
            'advice': 'Being kind is more rewarding than being right.'
        }
    }

@app.get('/messages')
async def get_message():
    message_day = requests.get('https://api.adviceslip.com/advice')

    json_data = json.loads(message_day.content)

    return json_data
    


if __name__ == '__main__':

    import uvicorn
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)

