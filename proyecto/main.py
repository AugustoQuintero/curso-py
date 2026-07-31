
from fastapi import FastAPI
from datetime import datetime
import pytz

app = FastAPI()

zonas = {'LA': "America/Los_Angeles",
         'CO': "America/Bogota",
         'NY': 'America/New_York', 
         'FR': 'Europe/Paris',
         'JP': 'Asia/Tokyo',
         'GE': "Europe/Berlin",
         'MX': 'America/Mexico_City'}

@app.get('/')
async def root():
    return {"Información":"Mi primera información"}

@app.get('/hora')
async def hora():
    return {'HORA': datetime.now()}

@app.get('/hora/{codigo}')
async def hora_pais(codigo : str):
    tz = zonas.get(codigo.upper())
    tz2 = pytz.timezone(tz)
    return {f'Hora en {tz}': datetime.now(tz2)}

