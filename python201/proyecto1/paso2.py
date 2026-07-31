from fastapi import FastAPI, HTTPException
from datetime import datetime
import pytz

app = FastAPI()

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
    return rutas_turisticas

# ---- NUEVO 02 ----
@app.get("/rutas/{ruta_id}")
async def obtener_ruta_por_id(ruta_id: int):
    """
    Devuelve los detalles de una ruta específica según su ID.
    """
    for ruta in rutas_turisticas:
        if ruta["id"] == ruta_id:
            return ruta
    raise HTTPException(status_code=404, detail="Ruta no encontrada")
# ---- --------- #

@app.get("/")
async def root():
    return {"Raiz": "No mucho que mostrar"}
