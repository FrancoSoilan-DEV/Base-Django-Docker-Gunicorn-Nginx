from .base import *  # noqa
import os

# DEBUG controlado por variable de entorno (pero True por defecto en local)
DEBUG = os.getenv("DJANGO_DEBUG", "True") == "True"

# ALLOWED_HOSTS desde variable de entorno (ej: "localhost,127.0.0.1"), o * en local
_allowed_hosts = os.getenv("DJANGO_ALLOWED_HOSTS")
if _allowed_hosts:
    ALLOWED_HOSTS = [h.strip() for h in _allowed_hosts.split(",")]
else:
    ALLOWED_HOSTS = ["*"]  # en local no nos vamos a complicar

# Base de datos PostgreSQL, leyendo todo desde env (con defaults razonables)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("POSTGRES_DB", "claroapp"),
        "USER": os.getenv("POSTGRES_USER", "admin"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", "admin"),
        "HOST": os.getenv("POSTGRES_HOST", "db"),  # nombre del servicio en docker-compose
        "PORT": os.getenv("POSTGRES_PORT", "5432"),
    }
}


