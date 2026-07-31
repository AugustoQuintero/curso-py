""" 
ayuda paso1
"""

from fastapi import FastAPI
from datetime import datetime
import pytz

app = FastAPI()

# Rutas turísticas disponibles
rutas_turisticos = [
    {"id": 1, "nombre": "Ruta Aventura Soacha", "tipo": "Aventura", "descripcion": "Recorrido por montañas y senderos."},
    {"id": 2, "nombre": "Ruta Cultural Soacha", "tipo": "Cultural", "descripcion": "Visita a monumentos históricos y museos."},
    {"id": 3, "nombre": "Ruta Natural Soacha", "tipo": "Natural", "descripcion": "Exploración de parques y zonas verdes."}
]

@app.get("/")
async def root():
    return {"Raiz": "No mucho que mostrar"}

@app.get("/rutas")
async def obtener_rutas():
    return rutas_turisticos
