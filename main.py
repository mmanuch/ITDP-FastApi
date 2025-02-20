from typing import Union
from routes import document, category, symbols, process, usuario
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
import os
import logging

# Configuración del logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("uvicorn")

# Inicialización de la app FastAPI
app = FastAPI()

# Endpoint de prueba
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Inclusión de routers
app.include_router(document.router)
app.include_router(category.router)
app.include_router(symbols.router)
app.include_router(process.router)
app.include_router(usuario.router)

# Configuración de variables de entorno para diferenciar entre desarrollo y producción
ENV = os.getenv("ENV", "development")  # Cambia entre "development" y "production"

# Configuración de orígenes permitidos
origins = ["*"] if ENV == "development" else ["http://51.178.73.104:1002"]
# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Orígenes permitidos según el entorno
    allow_credentials=True,  # Permitir cookies
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los encabezados HTTP
)

# Middleware adicional para registrar los orígenes de las solicitudes entrantes
@app.middleware("http")
async def log_origins(request: Request, call_next):
    origin = request.headers.get("origin")
    logger.info(f"Solicitud de origen: {origin}")
    response = await call_next(request)
    return response

