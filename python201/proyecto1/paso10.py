import httpx  # Importamos httpx para hacer peticiones externas
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from math import radians, sin, cos, sqrt, atan2

app = FastAPI()

class Ruta(BaseModel):
    id: int
    nombre: str
    tipo: str

rutas_turisticas = [
    {"id": 1, "nombre": "Circuito Histórico de Soacha", "tipo": "cultural"},
    {"id": 2, "nombre": "Sendero Laguna Blanca", "tipo": "natural"}
]

# ---- NUEVO 10: coordenada mas cercana ----
@app.get("/ricaurte/rutas/cercana")
async def obtener_ruta_mas_cercana(lat: float, lon: float):
    """
    Encuentra la ruta turística más cercana al punto dado (lat, lon).
    """
    url = "https://www.datos.gov.co/resource/6e4m-6mng.json"

    try:
        async with httpx.AsyncClient() as client:
            respuesta = await client.get(url)

        if respuesta.status_code != 200:
            raise HTTPException(status_code=respuesta.status_code, detail="Error al consultar la API externa")

        datos = respuesta.json()
        ruta_mas_cercana = None
        distancia_minima = float("inf")

        for sitio in datos:
            try:
                if "formato_google_maps" in sitio and sitio["formato_google_maps"].strip() != "":
                    lat_str, lon_str = sitio["formato_google_maps"].split(",")
                    lat_ruta = float(lat_str.strip())
                    lon_ruta = float(lon_str.strip())

                    # Calcular distancia usando la fórmula de Haversine
                    from math import radians, sin, cos, sqrt, atan2
                    R = 6371.0
                    dlat = radians(lat_ruta - lat)
                    dlon = radians(lon_ruta - lon)
                    a = sin(dlat / 2)**2 + cos(radians(lat)) * cos(radians(lat_ruta)) * sin(dlon / 2)**2
                    c = 2 * atan2(sqrt(a), sqrt(1 - a))
                    distancia = R * c

                    if distancia < distancia_minima:
                        distancia_minima = distancia
                        ruta_mas_cercana = sitio
                        ruta_mas_cercana["coordenadas"] = [lat_ruta, lon_ruta]
                        ruta_mas_cercana["distancia_km"] = round(distancia, 3)
            except:
                continue

        if ruta_mas_cercana:
            return {
                "origen_usuario": [lat, lon],
                "ruta_mas_cercana": ruta_mas_cercana
            }
        else:
            raise HTTPException(status_code=404, detail="No se encontraron rutas válidas con coordenadas.")

    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Error de conexión: {e}")
# --------------------------------------------------------------------------

@app.get("/ricaurte/rutas/distancia")
async def calcular_distancia(
    lat1: float, lon1: float,
    lat2: float, lon2: float
):
    """
    Calcula la distancia en kilómetros entre dos puntos geográficos usando la fórmula de Haversine.
    """
    # Radio de la Tierra en km
    R = 6371.0

    # Convertir grados a radianes
    lat1_rad = radians(lat1)
    lon1_rad = radians(lon1)
    lat2_rad = radians(lat2)
    lon2_rad = radians(lon2)

    # Diferencias
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # Fórmula de Haversine
    a = sin(dlat / 2)**2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distancia = R * c

    return {
        "distancia_km": round(distancia, 3),
        "origen": [lat1, lon1],
        "destino": [lat2, lon2]
    }

@app.get("/ricaurte/rutas")
async def obtener_rutas_ricaurte():
    """
    Consulta la API pública de Datos Abiertos y devuelve los sitios turísticos de Ricaurte.
    """
    url = "https://www.datos.gov.co/resource/6e4m-6mng.json"

    try:
        async with httpx.AsyncClient() as client:
            respuesta = await client.get(url)

        if respuesta.status_code == 200:
            datos = respuesta.json()

            rutas_con_coordenadas = []
            for sitio in datos:
                # Verificamos si existe y no está vacía
                if "formato_google_maps" in sitio and sitio["formato_google_maps"].strip() != "":
                    try:
                        # Dividimos el texto y convertimos a float
                        lat_str, lon_str = sitio["formato_google_maps"].split(",")
                        lat = float(lat_str.strip())
                        lon = float(lon_str.strip())
                        sitio["coordenadas"] = [lat, lon]  # Agregamos campo útil
                        rutas_con_coordenadas.append(sitio)
                    except ValueError:
                        # Saltamos si el formato es incorrecto
                        continue
            return {
                "total_original": len(datos),
                "con_coordenadas": len(rutas_con_coordenadas),
                "rutas": rutas_con_coordenadas
            }

        else:
            raise HTTPException(status_code=respuesta.status_code, detail="Error al consultar la API externa")

    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Error de conexión: {e}")

@app.get("/rutas")
async def obtener_rutas():
    return rutas_turisticas

@app.get("/rutas/{ruta_id}")
async def obtener_ruta_por_id(ruta_id: int):
    for ruta in rutas_turisticas:
        if ruta["id"] == ruta_id:
            return ruta
    raise HTTPException(status_code=404, detail="Ruta no encontrada")

@app.post("/rutas")
async def crear_ruta(ruta: Ruta):
    for r in rutas_turisticas:
        if r["id"] == ruta.id:
            raise HTTPException(status_code=400, detail="Ya existe una ruta con ese ID")
    rutas_turisticas.append(ruta.dict())
    return {"mensaje": "Ruta creada exitosamente", "ruta": ruta}

@app.put("/rutas/{ruta_id}")
async def actualizar_ruta(ruta_id: int, datos_actualizados: Ruta):
    for indice, ruta in enumerate(rutas_turisticas):
        if ruta["id"] == ruta_id:
            if datos_actualizados.id != ruta_id:
                raise HTTPException(status_code=400, detail="El ID del cuerpo debe coincidir con el de la URL")
            rutas_turisticas[indice] = datos_actualizados.dict()
            return {"mensaje": "Ruta actualizada", "ruta": datos_actualizados}
    raise HTTPException(status_code=404, detail="Ruta no encontrada")

@app.delete("/rutas/{ruta_id}")
async def eliminar_ruta(ruta_id: int):
    for indice, ruta in enumerate(rutas_turisticas):
        if ruta["id"] == ruta_id:
            ruta_eliminada = rutas_turisticas.pop(indice)
            return {"mensaje": "Ruta eliminada", "ruta": ruta_eliminada}
    raise HTTPException(status_code=404, detail="Ruta no encontrada")

@app.get("/")
async def root():
    return {"Raiz": "No mucho que mostrar"}
