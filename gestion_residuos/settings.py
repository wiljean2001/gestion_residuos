from pathlib import Path
from datetime import timedelta
from decouple import config
# import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "djoser",
    "corsheaders",
    "aplicaciones.reportes.apps.ReportesConfig",
    "aplicaciones.personal.apps.PersonalConfig",
    "aplicaciones.recolecciones.apps.RecoleccionesConfig",
    "aplicaciones.residuos.apps.ResiduosConfig",
    "aplicaciones.vehiculos.apps.VehiculosConfig",
    "aplicaciones.ubicaciones.apps.UbicacionesConfig",
    "aplicaciones.core.apps.CoreConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "gestion_residuos.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR.joinpath("frontend")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "gestion_residuos.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Define un directorio donde se almacenarán los archivos estáticos recolectados
# STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Custom user model
AUTH_USER_MODEL = "core.User"

# CORS configs
CORS_ALLOW_ALL_ORIGINS = True

# CORS_ALLOWED_ORIGINS = [
#     'http://localhost:8000',
# ]

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

# CORS_ALLOW_HEADERS = [
#     'accept',
#     'authorization',
#     'content-type',

# ]

# Email configs
# config('EMAIL_BACKEND')
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
MAILER_EMAIL_BACKEND = config("MAILER_EMAIL_BACKEND")
EMAIL_HOST = config("EMAIL_HOST")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_PORT = config("EMAIL_PORT")
EMAIL_USE_TLS = config("EMAIL_USE_TLS")
# EMAIL_USE_SSL = config('EMAIL_USE_SSL')
DEFAULT_FROM_EMAIL = config("EMAIL_HOST_USER")


# REST Framework configs
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}

# Simple JWT configs
SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("JWT",),
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    # 'ALGORITHM': 'HS256',
    # 'SIGNING_KEY': config('SECRET_KEY'),
}

# Djoser configs
DJOSER = {
    "SERIALIZERS": {
        "user_create": "aplicaciones.core.serializers.UserCreateSerializer",
        "current_user": "aplicaciones.core.serializers.UserSerializer",
        "user": "aplicaciones.core.serializers.UserSerializer",
    },
    "SEND_ACTIVATION_EMAIL": False,
    "ACTIVATION_URL": "auth/activate/?uid={uid}&token={token}",
    "PASSWORD_RESET_CONFIRM_URL": "auth/reset-password/?uid={uid}&token={token}",
    "PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND": True,
}

DOMAIN = "localhost:8000"
SITE_NAME = "COMUNIDAD TRAPEROS AGUILAS EMAUS"


STATICFILES_DIRS = (BASE_DIR.joinpath("frontend", "dist"),)
