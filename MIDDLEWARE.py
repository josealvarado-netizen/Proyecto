import random
import time
from fastapi import FastAPI, Request
app = FastAPI()
 #este middleware se ejecuta en cada peticion HTTP entrante
@app.middleware("http")
async def add_random_number(request: Request, call_next):
    inicio =time.time()
    
    #intercepta y pasa la peticion al siguiente manejador
    response = await call_next(request)
    
    #se ejecuta despues de que tu ruta genera la respuesta
    duracion = time.time() - inicio
    response.headers["X-Tiempo-Procesamiento"] = str(duracion)
    return response

@app.get("/cargar-datos")
async def cargar_datos():
    time.sleep(random.randint(a=3, b=9))  # Simula una tarea que tarda entre 0.5 y 2 segundos
    datos= {"datos":"cargados"}
    return datos

@app.get("/")
def leer_raiz():
    return {"mensaje": "Hola, mundo!"}

