from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import pytz

app = FastAPI()

# ---- NUEVO 03 ----
# Modelo de datos para validación de entrada
class Ruta(BaseModel):
    id: int
    nombre: str
    tipo: str
# ---- --------- #

rutas_turisticas = [
    {"id": 1, "nombre": "Circuito Histórico de Soacha", "tipo": "cultural"},
    {"id": 2, "nombre": "Sendero Laguna Blanca", "tipo": "natural"}
]

@app.get("/rutas")
async def obtener_rutas():
    return rutas_turisticas

@app.get("/rutas/{ruta_id}")
async def obtener_ruta_por_id(ruta_id: int):
    for ruta in rutas_turisticas:
        if ruta["id"] == ruta_id:
            return ruta
    raise HTTPException(status_code=404, detail="Ruta no encontrada")

# ---- NUEVO 03 ----
@app.post("/rutas")
async def crear_ruta(ruta: Ruta):
    """
    Crea una nueva ruta turística a partir de los datos enviados por el usuario.
    """
    # Verificar si ya existe una ruta con el mismo ID
    for r in rutas_turisticas:
        if r["id"] == ruta.id:
            raise HTTPException(status_code=400, detail="Ya existe una ruta con ese ID")

    rutas_turisticas.append(ruta.dict())  # Convertimos el objeto Pydantic a dict
    return {"mensaje": "Ruta creada exitosamente", "ruta": ruta}
# ---- --------- #

@app.get("/")
async def root():
    return {"Raiz": "No mucho que mostrar"}
