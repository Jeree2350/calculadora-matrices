from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configurar CORS para que el frontend pueda conectarse
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes poner "http://localhost:5173" si usas Vite
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class MatrizRequest(BaseModel):
    filas: int
    columnas: int

@app.post("/calcular")
def calcular_matriz(data: MatrizRequest):
    filas = data.filas
    columnas = data.columnas

    # Crear una matriz con valores incrementales
    matriz = [[(i * columnas) + j + 1 for j in range(columnas)] for i in range(filas)]

    return {"matriz": matriz}
