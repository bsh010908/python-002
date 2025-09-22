from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-tp2t7kmexvwk!9&yk43$ui-w=tc3*nw@m_s(0@6jf8+pzt1fq("
DEBUG = True
ALLOWED_HOSTS = []

# ======================
# Application definition
# ======================
INSTALLED_APPS = [
    # 🎨 Jazzmin 테마 (Admin UI 개선)
    "jazzmin",

    # Django 기본 앱들 (Jazzmin이 admin 확장하므로 반드시 필요)
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # MongoEngine + Admin
    "django_mongoengine",
    "django_mongoengine.mongo_admin",

    # 🚢 도메인 앱 (User, Ships, Ports 등)
    "myapp",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "myproject.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "myproject.wsgi.application"

# ======================
# ✅ MongoDB 연결 설정 (django-mongoengine 방식)
# ======================
MONGODB_DATABASES = {
    "default": {
        "name": "testdb",
        "host": "localhost",
        "port": 27017,
        # "username": "user",  # 필요 시 추가
        # "password": "pass",
    }
}

# ======================
# ✅ 인증/세션을 MongoDB에 저장
# ======================
SESSION_ENGINE = "django_mongoengine.sessions"
SESSION_SERIALIZER = "django_mongoengine.sessions.BSONSerializer"
AUTH_USER_MODEL = "myapp.User"  # 🚨 반드시 커스텀 User 모델 구현 필요

# ======================
# Password validation
# ======================
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ======================
# Internationalization
# ======================
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ======================
# Static files
# ======================
STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
