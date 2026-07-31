from fastapi import FastAPI, HTTPException
from math import radians, sin, cos, atan2, sqrt
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI()
app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
    )

@app.get('/ricaurte/rutas/cercana')
async def obtener_ruta_mas_cercana(lat:float, lon:float):
    url = 'https://www.datos.gov.co/resource/6e4m-6mng.json'
    async with httpx.AsyncClient() as cliente:
        respuesta = await cliente.get(url)
    if respuesta.status_code != 200:
        raise HTTPException(status_code=respuesta.status_code, detail='Error api externa')
    datos = respuesta.json()
    ruta_mas_cercana = None
    distancia_minima = float('inf')
    for sitio in datos:
        if 'formato_google_maps' in sitio and sitio['formato_google_maps'].strip() != '':
            lat_str, lon_str = sitio['formato_google_maps'].split(',')
            lat_ruta = float(lat_str.strip())
            lon_ruta = float(lon_str.strip())
            R = 6371.0
            dlat = radians(lat_ruta - lat)
            dlon = radians(lon_ruta - lon)
            a = sin(dlat/2)**2 + cos(lat_ruta) * cos(lat_ruta) * sin(dlon/2)**2
            c = 2 * atan2(sqrt(a), sqrt(1-a))
            d = R * c
            if d < distancia_minima:
                distancia_minima = d
                ruta_mas_cercana = sitio
                ruta_mas_cercana['coordenadas'] = [lat_ruta, lon_ruta]
                ruta_mas_cercana['distancia_k'] = round(d, 3)
    if ruta_mas_cercana:
        return {'origen': [lat, lon],
                'ruta_mas_cercana': ruta_mas_cercana}


@app.get('/ricaurte/rutas')
async def obtener_rutas_ricaurte():
    url = 'https://www.datos.gov.co/resource/6e4m-6mng.json'
    try:
        async with httpx.AsyncClient() as cliente:
            respuesta = await cliente.get(url)
            if respuesta.status_code == 200:
                datos = respuesta.json()
                rutas_con_coordenadas = []
                for sitio in datos:
                    if 'formato_google_maps' in sitio and sitio['formato_google_maps'].strip() != '':
                        try:
                            lat_str, lon_str = sitio['formato_google_maps'].split(',')
                            lat = float(lat_str.strip())
                            lon = float(lon_str.strip())
                            sitio['coordenadas'] = [lat, lon]
                            rutas_con_coordenadas.append(sitio)
                        except ValueError:
                            continue
                return {'total_original': len(datos),
                        'con_coordenadas': len(rutas_con_coordenadas),
                        'rutas': rutas_con_coordenadas}
            else:
                raise HTTPException(status_code=respuesta.status_code, detail='Error al consultar')
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f'Error de conexión: {e}')

@app.get('/ricaurte/rutas/distancia')
async def calcular_distancia(lat1:float, lon1:float, lat2:float, lon2:float):
    R = 6371.0
    lat1_rad = radians(lat1)
    lon1_rad = radians(lon1)
    lat2_rad = radians(lat2)
    lon2_rad = radians(lon2)
    # distancia
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    # Haversine
    a = sin(dlat/2)**2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    d = R * c
    return {'distancia': round(d, 3),
            'origen': [lat1, lon1],
            'destino': [lat2, lon2]}


