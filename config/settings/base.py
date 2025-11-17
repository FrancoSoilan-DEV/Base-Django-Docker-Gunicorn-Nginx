from pathlib import Path

# BASE_DIR hace referencia a cual es la carpeta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Definición: SECRET_KEY: cadena aleatoria usada por Django para firmar cookies, sesiones, tokens CSRF y otros datos criptográficos.

# Para qué sirve: garantiza la integridad y confidencialidad de firmas (p. ej. sessions, mensajes firmados, password reset tokens).

# Riesgo si se filtra: un SECRET_KEY comprometido permite falsificar cookies/tokens y atacar la seguridad de la app — por eso nunca debe ponerse en un repositorio público.

SECRET_KEY = 'django-insecure-b-_2_(@m^c(m@rj*rleb!pt)$y5j$_0qiel7526_^wcn!hsnhm'


# MANEJO DE APPS

# apps de django
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)
# apps locales
LOCAL_APPS = (
 
)
# apps de terceros
THIRD_PARTY_APPS = (
    'rest_framework',
)

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS


# Definición: componente que se ejecuta entre la petición del cliente y la vista, y también entre la vista y la respuesta. Actúa como una capa global que puede inspeccionar/alterar request y response.

# Propósito: tareas transversales a muchas vistas: autenticación, sesiones, CSRF, cabeceras de seguridad, compresión, logging, redirecciones, etc.

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Definición: ROOT_URLCONF: nombre (string) del módulo Python que contiene el enrutador raíz de URL de tu proyecto.

# Función: Django importa ese módulo y busca la variable urlpatterns para resolver las peticiones entrantes a vistas. Es el punto de entrada del sistema de URLs.

ROOT_URLCONF = 'config.urls'

# Definición: TEMPLATES es la configuración que le dice a Django cómo y dónde cargar y renderizar plantillas HTML (templating engines).

# Dónde vive: en tu settings (p. ej. base.py). Django lee esta lista al arrancar y registra los motores (por defecto el motor de Django y opcionalmente Jinja2).

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # <── carpeta templates de la raíz
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI_APPLICATION es la ruta (string) al "callable" WSGI que Django exporta para que un servidor WSGI (p. ej. Gunicorn, uWSGI, mod_wsgi) pueda llamar a tu aplicación. En tu configuración: WSGI_APPLICATION = 'config.wsgi.application' significa "importa config.wsgi y usa la variable application".
# Qué es WSGI (breve):

# WSGI = Web Server Gateway Interface, estándar de Python para aplicaciones web síncronas. El servidor recibe la petición HTTP y la pasa al callable WSGI; el callable devuelve la respuesta HTTP.

WSGI_APPLICATION = 'config.wsgi.application'


# Explicación completa sobre AUTH_PASSWORD_VALIDATORS en Django:

# ¿Qué es?
# AUTH_PASSWORD_VALIDATORS es una lista de validadores que Django usa para comprobar la fortaleza/validez de las contraseñas cuando se crean o cambian (por ejemplo en UserCreationForm, PasswordChangeForm, admin, o si llamas a validate_password() manualmente).

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Define el idioma por defecto que usará Django para la internacionalización/locale (traducciones automáticas de textos integrados y formatos de fecha/número).
# Si tu app es en español, cámbialo a algo como 'es' o 'es-es' o 'es-ES' según prefieras; por ejemplo: LANGUAGE_CODE = 'es-ES'.
# No confundir con las traducciones de tus textos
LANGUAGE_CODE = 'en-us'

# Zona horaria por defecto que Django usará para interpretar y mostrar tiempos cuando no hay zona explícita.
TIME_ZONE = 'UTC'

# Activa el framework de internacionalización de Django (traducción de textos).
# Si está False, las utilidades de traducción no se aplican y LANGUAGE_CODE tiene menos efecto. Mantén True si planeas soportar otros idiomas o usar mensajes traducibles.
USE_I18N = True

# Habilita soporte de zonas horarias: Django almacenará datetimes en UTC en la base de datos y usará objetos timezone-aware.
# Recomendado dejar True en la mayoría de proyectos (facilita despliegue multi-zona y evita errores con horarios).
USE_TZ = True

# Establece el tipo de campo PK que Django añade automáticamente a modelos que no definen id.
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Estáticos
STATIC_URL = '/static/'

# Donde collectstatic deja todo para producción (Nginx apunta aquí)
STATIC_ROOT = BASE_DIR / 'static_root'

# Carpeta donde tú tienes los archivos fuente (assets/css, assets/js, assets/img)
STATICFILES_DIRS = [
    BASE_DIR / 'assets',
]

# (Opcional) Media si la vas a usar
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

