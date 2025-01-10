import os
from pathlib import Path

# مسیر اصلی پروژه
BASE_DIR = Path(__file__).resolve().parent.parent

# کلید مخفی (برای محیط تولید تغییر دهید)
SECRET_KEY = 'your-secret-key'

# حالت دیباگ
DEBUG = False

# هاست‌های مجاز
ALLOWED_HOSTS = []

# اپلیکیشن‌های نصب‌شده
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'songs',  # اپلیکیشن اصلی پروژه
]

# میان‌افزارها
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# فایل تنظیمات URLها
ROOT_URLCONF = 'music_player.urls'

# تنظیمات قالب‌ها
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # مسیر پوشه قالب‌ها
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

# برنامه WSGI
WSGI_APPLICATION = 'music_player.wsgi.application'

# تنظیمات پایگاه داده
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# تنظیمات پسورد
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

# تنظیمات بین‌المللی
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# تنظیمات فایل‌های استاتیک
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# تنظیمات فایل‌های رسانه‌ای
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# تنظیمات مسیرهای ورود و خروج
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = 'song_list'
LOGOUT_REDIRECT_URL = '/'

# تنظیمات پیش‌فرض برای فیلدهای خودکار
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
