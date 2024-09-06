from typing import Union
from routes import document, category, symbols, process, usuario
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(document.router)
app.include_router(category.router)
app.include_router(symbols.router)
app.include_router(process.router)
app.include_router(usuario.router)


# Lista de orígenes permitidos (como cadenas).
origins = [
    "http://localhost:3000",  # Asegúrate de cambiar esto por tus propios orígenes
]

# Configuración del middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Los orígenes que tienen permitido hacer solicitudes
    allow_credentials=True,  # Permite que se envíen cookies
    allow_methods=["*"],  # Permite todos los métodos HTTP
    allow_headers=["*"],  # Permite todos los encabezados HTTP
)
