from fastapi import FastAPI, HTTPException
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

@app.get("/rutas/{id}")
async def obtener_ruta(id: int):
    # Buscar la ruta por ID
    ruta = next((ruta for ruta in rutas_turisticos if ruta["id"] == id), None)
    
    # Si la ruta no existe, lanzamos una excepción 404
    if ruta is None:
        raise HTTPException(status_code=404, detail="Ruta no encontrada")
    
    return ruta
