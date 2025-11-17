# Instrucciones para crear la imagen del proyecto, crea un contenedor donde tendremos la aplicacion

# Le dices a Docker: empieza desde una imagen que ya tiene Linux + Python 3.12 instalado.
# slim = versión más ligera (menos paquetes del sistema, imagen más pequeña).
FROM python:3.12-slim

# ===== Variables de entorno útiles =====
# Evita que pip muestre avisos de actualización cada vez que se ejecuta.
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
# Evita que Python genere archivos .pyc y __pycache__/
ENV PYTHONDONTWRITEBYTECODE=1
# Python imprime logs sin buffer (logs inmediatos)
ENV PYTHONUNBUFFERED=1

# ===== Paquetes del sistema (NECESARIOS para psycopg2) =====
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo dentro del contenedor.
WORKDIR /code

# ===== Dependencias Python =====
# Copia la carpeta de tu proyecto requirements/ (la que ves en VSCode) a la ruta /requirements/ dentro del contenedor.
COPY requirements/ /requirements/
# Ejecuta, durante el build, la instalación de dependencias de producción.
RUN pip install --no-cache-dir -r /requirements/prod.txt

# ===== Copiar el proyecto =====
# ( . . -> copia todo lo que esta aqui dentro del directorio de trabajo /code)
COPY . .

# (Opcional) Indicar qué puerto "expone" este contenedor
EXPOSE 8000

# ===== Comando de arranque: Gunicorn =====
# IMPORTANTE: cambia config.wsgi por el nombre real de tu módulo wsgi (mira tu carpeta "config/" o similar)
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
