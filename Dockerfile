# Usar una imagen base oficial de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos de tu aplicación al contenedor
COPY . /app

# Crear un entorno virtual
RUN python -m venv /venv

# Instalar las dependencias dentro del entorno virtual
RUN /venv/bin/pip install --no-cache-dir -r requirements.txt

# Exponer el puerto en el que FastAPI va a escuchar
EXPOSE 8001

# Comando para iniciar el servidor de FastAPI con uvicorn
CMD ["/venv/bin/uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
