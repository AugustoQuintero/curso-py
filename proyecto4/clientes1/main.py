"""  
Api 01:
"""

from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def root():
    return {"Info de inicio": "Primera página con contenido inicial."}

