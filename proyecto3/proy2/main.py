from datetime import datetime
from fastapi import FastAPI
import pytz
from pydantic import BaseModel

class Cliente(BaseModel):
    nombre: str
    direccion : str
    edad: int

zona = {'co': 'America/Bogota'}

app = FastAPI()

@app.get('/')
async def root():
    return {"Message": "Este es un mensaje..."}

@app.get('/hora')
async def hora():
    return {"Hora sin pais": datetime.now()}

@app.get('/hora/{pais}')
async def hora(pais : str):
    tz = pytz.timezone(zona.get(pais))
    return {"Hora": datetime.now(tz)}

@app.post('/clientes')
async def crear_cliente(datos_cliente : Cliente):
    return datos_cliente