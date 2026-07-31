import requests
from fastapi import FastAPI, HTTPException
from math import radians, sin, cos, sqrt, atan2

app = FastAPI()

# Datos de ejemplo con coordenadas de puntos turísticos en Soacha
rutas_turisticos = [
    {"id": 1, "nombre": "Ruta Aventura Soacha", "tipo": "Aventura", "descripcion": "Recorrido por montañas y senderos.", "ubicacion": {"lat": 4.5773, "lon": -74.1957}},
    {"id": 2, "nombre": "Ruta Cultural Soacha", "tipo": "Cultural", "descripcion": "Visita a monumentos históricos y museos.", "ubicacion": {"lat": 4.5912, "lon": -74.2305}},
    {"id": 3, "nombre": "Ruta Natural Soacha", "tipo": "Natural", "descripcion": "Exploración de parques y zonas verdes.", "ubicacion": {"lat": 4.6017, "lon": -74.2368}}
]

@app.get("/rutas")
async def obtener_rutas():
    return rutas_turisticos

@app.get("/rutas/{id}")
async def obtener_ruta(id: int):
    ruta = next((ruta for ruta in rutas_turisticos if ruta["id"] == id), None)
    if ruta is None:
        raise HTTPException(status_code=404, detail="Ruta no encontrada")
    return ruta

# Función para calcular la distancia entre dos puntos usando la fórmula de Haversine
def calcular_distancia(lat1, lon1, lat2, lon2):
    R = 6371.0  # Radio de la Tierra en kilómetros

    # Convertir grados a radianes
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    # Fórmula de Haversine
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distancia = R * c  # Distancia en kilómetros
    return distancia

@app.get("/rutas/{id}/distancia")
async def obtener_distancia(id: int, destino_id: int):
    # Obtener las rutas por ID
    ruta_origen = next((ruta for ruta in rutas_turisticos if ruta["id"] == id), None)
    ruta_destino = next((ruta for ruta in rutas_turisticos if ruta["id"] == destino_id), None)

    if ruta_origen is None or ruta_destino is None:
        raise HTTPException(status_code=404, detail="Una de las rutas no fue encontrada")

    # Obtener las coordenadas de las rutas (latitud y longitud)
    lat_origen = ruta_origen["ubicacion"]["lat"]
    lon_origen = ruta_origen["ubicacion"]["lon"]
    lat_destino = ruta_destino["ubicacion"]["lat"]
    lon_destino = ruta_destino["ubicacion"]["lon"]

    # Calcular la distancia entre las rutas
    distancia = calcular_distancia(lat_origen, lon_origen, lat_destino, lon_destino)

    # Estimación del tiempo de viaje (suponiendo una velocidad promedio de 40 km/h)
    tiempo_estimado = distancia / 40  # Tiempo en horas
    tiempo_estimado = round(tiempo_estimado * 60)  # Convertimos a minutos

    return {
        "origen": ruta_origen["nombre"],
        "destino": ruta_destino["nombre"],
        "distancia": f"{round(distancia, 2)} km",
        "tiempo_estimado": f"{tiempo_estimado} mins"
    }
