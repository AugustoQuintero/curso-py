import httpx  # 👈 Importamos httpx para hacer peticiones externas
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Ruta(BaseModel):
    id: int
    nombre: str
    tipo: str

rutas_turisticas = [
    {"id": 1, "nombre": "Circuito Histórico de Soacha", "tipo": "cultural"},
    {"id": 2, "nombre": "Sendero Laguna Blanca", "tipo": "natural"}
]

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
            # -- NUEVO 7: Filtrar registros con coordenadas en formato_google_maps ----
            rutas_con_coordenadas = [
                sitio for sitio in datos
                if "formato_google_maps" in sitio and sitio["formato_google_maps"].strip() != ""
            ]

            return {
                "total_original": len(datos),
                "con_coordenadas": len(rutas_con_coordenadas),
                "rutas": rutas_con_coordenadas
            }
            # return {"cantidad": len(datos), "rutas": datos}
            # --------------------------------------------------------------------------
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
