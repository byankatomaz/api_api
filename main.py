from fastapi import FastAPI, HTTPException, status
import json
import requests
from random import randrange

app = FastAPI()



message = {
    "frasesDay": [
        {
            'id': 1,
            'advice': 'Lembre-se de sempre contar quantos unicórnios passaram voando pela sua janela antes do café da manhã.'
        },
        {
            'id': 2, 
            'advice': 'Hoje, seja como um abacaxi: tenha espinhas, mas também seja doce por dentro.'
        },
        {
            'id': 3, 
            'advice': 'Nunca deixe de abraçar árvores, elas são ótimas ouvintes.'
        },
        {
            'id': 4, 
            'advice': 'Antes de tomar decisões importantes, consulte seu gato e veja como ele está piscando.'
        },
        {
            'id': 5,
            'new_advice': 'Acorde sorrindo e agradeça ao sol por fornecer Wi-Fi grátis.'
        },
        {
            'id': 6, 
            'advice': 'Seja uma sereia em um mundo cheio de peixes, mas não se esqueça de levar protetor solar.'
        },
        {
            'id': 7, 
            'advice': 'Dance com seus sapatos de caminhada antes de calçá-los para uma jornada épica.'
        },
         {
            'id': 8, 
            'advice': 'Hoje, faça uma pausa para abraçar seu travesseiro e agradecer por todas as noites de sono tranquilas.'
        },
        {
            'id': 9, 
            'advice': 'Não se esqueça de alimentar seus sonhos com cereais de arco-íris todas as manhãs.'
        },
           {
            'id': 10, 
            'advice': 'Lembre-se de que as nuvens também têm sonhos, então não as perturbe.'
        }
    ]
}




@app.get('/messages')
async def get_message():
    
    index = randrange(len(message['frasesDay']))
    
    message_day = requests.get('https://api.adviceslip.com/advice')

    dados = json.loads(message_day.content)
    
    dados['slip'] = message['frasesDay'][index]

    return dados


if __name__ == '__main__':

    import uvicorn
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)

