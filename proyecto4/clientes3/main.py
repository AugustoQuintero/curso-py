""" 
API 03
"""
from fastapi import FastAPI
from datetime import datetime
import pytz

app = FastAPI()

dichora = {"CO": "America/Bogota"}

@app.get("/")
async def root():
    return {"Raiz": "No mucho que mostrar"}

@app.get("/hora")
async def hora():
    return {"Fecha y hora actual": datetime.now(),
            "Fecha": datetime.now().date(),
            "Hora": datetime.now().time()}

# Con variables:
@app.get("/hora/{pais}")
async def horapais(pais : str):
    tz = pytz.timezone(dichora.get(pais.upper()))
    datetime.now(tz)
    return datetime.now(tz).strftime("%d / %m / %Y hora: %I : %M : %S %p")