"""
Django settings for megacenter project.
"""
import dj_database_ur
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------
# 🔐 Безопасность
# -------------------------
SECRET_KEY = 'django-insecure-yk!fxq3-)k!*^fddgb6fhx*yyct)w!g0^elr6vom-#v7ad#hie'

# ⚠️ В продакшене нужно отключить DEBUG
DEBUG = True

ALLOWED_HOSTS = ['megacenter.onrender.com', '127.0.0.1', 'localhost']



# -------------------------
# 📦 Приложения
# -------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'reviews.apps.ReviewsConfig',
    'accounts',
]

# -------------------------
# 🌐 Middleware
# -------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'megacenter.urls'

# -------------------------
# 🎨 Templates
# -------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # если позже добавишь общие шаблоны
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

WSGI_APPLICATION = 'megacenter.wsgi.application'

# -------------------------
# 💾 База данных (PostgreSQL на Render)
# -------------------------

DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://megacenter_db_user:XoLDXNlAS6yH1ixC7k81mkxEV0Tc1YIO@dpg-d40e8hfgi27c73fgahj0-a.frankfurt-postgres.render.com/megacenter_db',
        conn_max_age=600,
        ssl_require=True
    )
}
# -------------------------
# 🔑 Валидация паролей
# -------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -------------------------
# 🌍 Локализация
# -------------------------
LANGUAGE_CODE = 'ru'      # чтобы админка и интерфейс были на русском
TIME_ZONE = 'Asia/Tashkent'
USE_I18N = True
USE_TZ = True

# -------------------------
# 📁 Статические и медиа файлы
# -------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]  # папка с твоими исходными статическими файлами
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')    # сюда Django соберёт всё после collectstatic

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# -------------------------
# 📧 Почта (для уведомлений)
# -------------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'  # или другой провайдер
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_HOST_USER = '0zod.susu@gamil.com'   # твой почтовый адрес
EMAIL_HOST_PASSWORD = 'Sus0zod37'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# -------------------------
# 🧩 Разное
# -------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

