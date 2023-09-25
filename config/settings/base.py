#En este archivo ira la configuración base del proyecto.

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i0n&$uz4gf(nawukhrdo6kc2=%(@kyvxftl*ksinuf2ocybm71'

# # Application definition
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # local apps - aplicaciones que estamos creando.
    'apps.departament',
    'apps.employee',
    'apps.home',
    'apps.user',
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
        "employee.shifts": "far fa-calendar-plus",
        "employee.employee": "fas fa-address-card",
        "user.user": "far fa-address-card",
    },
    }

JAZZMIN_UI_TWEAKS = {
    "theme": "darkly",
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
