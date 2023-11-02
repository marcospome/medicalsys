#En este archivo ira la configuración base del proyecto.

from pathlib import Path
import os
import json
from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# --- Secret Json ---
with open("secret.json") as f:
    secret = json.loads(f.read())

def get_secret(secret_name, secrets=secret):
    try:
        return secrets[secret_name]
    except:
        msg = "la variable %s no existe" % secret_name
        raise ImproperlyConfigured(msg)
SECRET_KEY = get_secret('SECRET_KEY')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'django-insecure-i0n&$uz4gf(nawukhrdo6kc2=%(@kyvxftl*ksinuf2ocybm71'

# # Application definition
INSTALLED_APPS = [
    'jazzmin',
    'ckeditor',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # local apps - aplicaciones creadas.
    'apps.home',
    'apps.departament',
    'apps.appointment',
    'apps.employee',
    'apps.patient',
    'apps.base',
]

JAZZMIN_SETTINGS = {
    "site_title": "MedicalSys",
    "site_header": "Library",
    "site_brand": "MedicalSys",
    "site_logo": "/img/logo2.png",
    "site_icon": "/img/logo2.png",
    "welcome_sign": "Ingresar las credenciales de administrador",
    "changeform_format": "carousel",
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "departament.departament": "fas fa-hospital-user",
        "employee.employee": "fas fa-address-card",
        "patient.tratamientomedico": "fas fa-notes-medical",
        "patient.medicacion": "fas fa-prescription-bottle",
        "patient.paciente": "fas fa-user-injured",
        "patient.domicilio": "fas fa-home",
        "patient.parroquia": "fas fa-church",
        "patient.referente": "fas fa-cross",
        "patient.telefono": "fas fa-phone",
        "patient.tipotelefono": "fas fa-tty",
        "patient.pacientetratamientomedico": "fas fa-laptop-medical",
        "patient.certificado": "fas fa-print",
        "patient.tipocertificado": "fas fa-stamp",
    },
    }


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'
