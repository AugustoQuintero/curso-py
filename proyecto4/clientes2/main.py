"""
API 02 
"""
from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
async def root():
    return {"Iniciando": "Texto inicial."}

@app.get("/hora")
async def hora():
    return {"Fecha": datetime.now().date(),
            "Hora": datetime.now().time(),
            "Con formato": datetime.now().strftime('%d / %m / %Y'),
            "Con formato 2": datetime.now().strftime('%I : %M : %S %p')}


