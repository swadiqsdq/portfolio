"""
Complete Django settings for portfolio project deployment on Render.
Includes Time Zone, Password Validation, and Production Static File handling.
"""

from pathlib import Path
import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# ----------------------------------------------------------------------
# 1. CORE PRODUCTION SETTINGS & SECURITY
# ----------------------------------------------------------------------

# Use environment variables for secrets and debug control
IS_PRODUCTION = os.environ.get('IS_PRODUCTION', 'False') == 'True'

# SECURITY WARNING: Fetch SECRET_KEY securely from environment variable (MUST be set on Render)
SECRET_KEY = os.environ.get('SECRET_KEY', 'mi9!_vssd2q294m&aorwoh(_8$evjt3*$ret28w9xqf6c+vcuc')

# Set DEBUG based on the environment variable
DEBUG = not IS_PRODUCTION

# ALLOWED_HOSTS must contain your Render URL when DEBUG is False
if DEBUG:
    ALLOWED_HOSTS = ['*'] # Allows all hosts in local development
else:
    # Read comma-separated hosts from environment variable (set on Render)
    ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # --- YOUR APPS ---
    'app',
    'account',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # --- WhiteNoise middleware MUST be placed here ---
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'portfolio.wsgi.application'

# ----------------------------------------------------------------------
# 2. DATABASE CONFIGURATION (SQLite - Requires Persistent Disk on Render!)
# ----------------------------------------------------------------------
# WARNING: If you are not using a Persistent Disk on Render, your data will be lost.

# If using a Persistent Disk, update the 'NAME' path to the mount point (e.g., /opt/render/project/src/disk_data/db.sqlite3)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ----------------------------------------------------------------------
# 3. PASSWORD VALIDATION (Authentication)
# ----------------------------------------------------------------------
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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


# ----------------------------------------------------------------------
# 4. INTERNATIONALIZATION & TIME ZONE
# ----------------------------------------------------------------------
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

# Set your preferred time zone here (e.g., 'America/New_York', 'Asia/Kolkata')
TIME_ZONE = 'UTC' # Keeping UTC as a default best practice

USE_I18N = True

USE_TZ = True # Use timezone-aware datetimes

# ----------------------------------------------------------------------
# 5. STATIC FILES CONFIGURATION (WhiteNoise Fix)
# ----------------------------------------------------------------------

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]
STATIC_URL = '/static/'

# The destination folder for 'collectstatic'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Use the modern Django 4.2+ STORAGES setting for WhiteNoise optimization
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        # The key to serving static files correctly in production
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# ----------------------------------------------------------------------
# 6. MEDIA FILES CONFIGURATION (User Uploads)
# ----------------------------------------------------------------------
# WARNING: Media files will be lost on deploy without S3/Cloud Storage or a Persistent Disk.

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "uploads"

# ----------------------------------------------------------------------
# 7. MISC SETTINGS
# ----------------------------------------------------------------------

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Session settings
# 5 minutes = 300 seconds
SESSION_COOKIE_AGE = 300
# If user closes the browser, session ends
SESSION_EXPIRE_AT_BROWSER_CLOSE = True