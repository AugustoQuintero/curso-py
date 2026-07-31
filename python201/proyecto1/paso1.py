from fastapi import FastAPI
from datetime import datetime
import pytz

app = FastAPI()

# ---- NUEVO 01 ----
# Simulación de datos en memoria mientras conectamos la API externa
rutas_turisticas = [
    {
        "id": 1,
        "nombre": "Circuito Histórico de Soacha",
        "tipo": "cultural"
    },
    {
        "id": 2,
        "nombre": "Sendero Laguna Blanca",
        "tipo": "natural"
    }
]

@app.get("/rutas")
async def obtener_rutas():
    """
    Devuelve la lista completa de rutas turísticas disponibles.
    Por ahora trabajamos con datos simulados (mock) para centrarnos
    en la estructura del endpoint.
    """
    return rutas_turisticas
# ---- --------- #

@app.get("/")
async def root():
    return {"Raiz": "No mucho que mostrar"}
