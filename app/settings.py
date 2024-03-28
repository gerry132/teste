# -*- coding: utf-8 -*-
"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os

from dotenv import load_dotenv

TRUE = ["1", "True", "true", 1, True]

load_dotenv()

# Name of root directory, directory with settings.pt in it

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

DEBUG_TOOLBAR = os.environ.get("DEBUG_TOOLBAR", "0") in TRUE

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'os.environ["SECRET_KEY"]'


# SECURITY WARNING: don't run with debug turned on in production!
debug_on = os.environ.get("DEBUG")

if debug_on == '0':
    DEBUG = True
else:
    DEBUG = True

ALLOWED_HOSTS = ["*"]

# to disable the check
DATA_UPLOAD_MAX_NUMBER_FIELDS = None

# Application definition

INSTALLED_APPS = [
    #
    "app",
    "health_check",
    "cib_board",
    "cib_documents",
    "cib_form",
    "cib_images",
    "cib_users",
    "cib_search",
    "cib_utils",
    "cib_home",
    "cib_jobs",
    "cib_pages",
    "cib_navigation",
    "cib_content_page",
    "cib_news_page",
    "cib_news_content_page",
    #
    "wagtail_localize",
    "wagtail_localize.locales",
    "wagtail.contrib.forms",
    "wagtail.contrib.modeladmin",
    "wagtail.contrib.redirects",
    "wagtail.contrib.routable_page",
    "wagtail.contrib.settings",
    "wagtail.contrib.search_promotions",
    "wagtail.contrib.table_block",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    "wagtailaccessibility",
    "wagtailmedia",
    "wagtail.contrib.typed_table_block",
    "wagtail.api.v2",
    "captcha",
    "wagtailcaptcha",
    "modelcluster",
    "taggit",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    "pattern_library",
    "rest_framework",
    "corsheaders",
    "cib_project_styleguide.apps.ProjectStyleguideConfig",
    "wagtail.contrib.simple_translation",
    "wagtailcache",
    "tinymce",
    "wagtailtinymce",
]

if DEBUG_TOOLBAR is True:
    INSTALLED_APPS += [
        "debug_toolbar",
    ]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    # Wagtail extra
    "django.middleware.locale.LocaleMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
    "wagtailcache.cache.UpdateCacheMiddleware",
    "wagtailcache.cache.FetchFromCacheMiddleware",
    # "debug_toolbar.middleware.DebugToolbarMiddleware"
]

if DEBUG_TOOLBAR is True:
    MIDDLEWARE += [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]

ROOT_URLCONF = "app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PROJECT_DIR, "templates"),
            os.path.join(BASE_DIR, "templates"),
            "templates",
        ],
        "OPTIONS": {
            'loaders': [
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ]),
            ],
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # Wagtail extra
                "wagtail.contrib.settings.context_processors.settings",
                "django.template.context_processors.i18n",
                # custom processors
                "cib_utils.context_processors.local_languages",
            ],
            "builtins": ["pattern_library.loader_tags"],
        },
    },
]

# Django Pattern Library
PATTERN_LIBRARY_ENABLED = os.environ.get("PATTERN_LIBRARY_ENABLED", "0") in TRUE
PATTERN_LIBRARY = {
    "SECTIONS": (
        ("atoms", ["patterns/atoms"]),
        ("molecules", ["patterns/molecules"]),
        ("pages", ["patterns/pages"]),
        ("organisms", ["patterns/organisms"]),
    ),
    "TEMPLATE_SUFFIX": ".html",
    "PATTERN_BASE_TEMPLATE_NAME": "patterns/base.html",
    "BASE_TEMPLATE_NAMES": ["patterns/base_page.html"],
}


# In production, email is handled with Amazon SES
if "EMAIL_BACKEND" in os.environ:
    EMAIL_BACKEND = os.environ["EMAIL_BACKEND"]
else:
    EMAIL_BACKEND = "django_ses.SESBackend"

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


DATABASE_URL = os.environ.get("DATABASE_URL", None)
DATABASES = {}

if DATABASE_URL in [None, "None", ""]:
    DATABASES["default"] = {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(PROJECT_DIR, "db.sqlite3"),
    }
else:
    import dj_database_url

    DATABASES["default"] = dj_database_url.config(conn_max_age=600)

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

VALIDATOR_ROOT = "django.contrib.auth.password_validation"

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": f"{VALIDATOR_ROOT}.UserAttributeSimilarityValidator"},
    {"NAME": f"{VALIDATOR_ROOT}.MinimumLengthValidator"},
    {"NAME": f"{VALIDATOR_ROOT}.CommonPasswordValidator"},
    {"NAME": f"{VALIDATOR_ROOT}.NumericPasswordValidator"},
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

STATIC_ROOT = os.path.join(PROJECT_DIR, "static")
STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, "cib_home")
]


STATIC_URL = "/static/"
MEDIA_ROOT = os.path.join(PROJECT_DIR, "media")
MEDIA_URL = "/media/"

#

USE_CACHE = os.environ.get("USE_CACHE", "0") in TRUE
if USE_CACHE is True:
    CACHE_ADDRESS = os.environ["CACHE_ADDRESS"]
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": f"redis://{CACHE_ADDRESS}",
            "OPTIONS": {
                "IGNORE_EXCEPTIONS": True,
                "SOCKET_CONNECT_TIMEOUT": 2,  # seconds
                "SOCKET_TIMEOUT": 2,  # seconds
                "CONNECTION_POOL_KWARGS": {},
            },
        }
    }
    DJANGO_REDIS_LOG_IGNORED_EXCEPTIONS = True

# # https://docs.djangoproject.com/en/stable/ref/settings/#secure-ssl-redirect
# SECURE_SSL_REDIRECT = False


# # https://docs.djangoproject.com/en/stable/ref/settings/#secure-proxy-ssl-header
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# # https://docs.djangoproject.com/en/stable/ref/settings/#secure-hsts-seconds
# DEFAULT_HSTS_SECONDS = 30 * 24 * 60 * 60  # 30 days
# SECURE_HSTS_SECONDS = int(env.get('SECURE_HSTS_SECONDS', DEFAULT_HSTS_SECONDS))


# # https://docs.djangoproject.com/en/3.2/ref/settings/#secure-hsts-include-subdomains
# SECURE_HSTS_INCLUDE_SUBDOMAINS = False


# # https://docs.djangoproject.com/en/stable/ref/settings/#secure-browser-xss-filter
# SECURE_BROWSER_XSS_FILTER = True


# # https://docs.djangoproject.com/en/stable/ref/settings/#secure-content-type-nosniff
# SECURE_CONTENT_TYPE_NOSNIFF = True


# Wagtail DRF
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
    )
}
# https://pypi.org/project/django-cors-headers/
CORS_ALLOW_ALL_ORIGINS = True
if CORS_ALLOW_ALL_ORIGINS is False:
    CORS_ALLOWED_ORIGINS = os.environ["CORS_ALLOWED_ORIGINS"].split(",")
DEBUG_TOOLBAR = True
if DEBUG_TOOLBAR is True:
    INTERNAL_IPS = [
        "127.0.0.1",
        "localhost",
    ]

#

ALLOW_MAIL = os.environ.get("ALLOW_MAIL", "0") in TRUE
if ALLOW_MAIL is True:
    EMAIL_HOST = os.environ["EMAIL_HOST"]
    EMAIL_PORT = int(os.environ.get("EMAIL_PORT", "587"))
    EMAIL_HOST_USER = os.environ["EMAIL_HOST_USER"]
    EMAIL_HOST_PASSWORD = os.environ["EMAIL_HOST_PASSWORD"]
    EMAIL_USE_TLS = True
    EMAIL_SUBJECT_PREFIX = os.environ["EMAIL_SUBJECT_PREFIX"]
    SERVER_EMAIL = DEFAULT_FROM_EMAIL = os.environ["SERVER_EMAIL"]

if "DEFAULT_FROM_EMAIL" in os.environ:
    DEFAULT_FROM_EMAIL = os.environ["DEFAULT_FROM_EMAIL"]

# Wagtail settings

WAGTAIL_CONTENT_LANGUAGES = LANGUAGES = [
    ("en", "English"),
    ("ga", "Irish"),
]

LOCALE_PATHS = [
    os.path.join(PROJECT_DIR, "locale"),
]

WAGTAIL_LOCALIZE_DEFAULT_TRANSLATION_MODE = "simple"

# AWS

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_SES_REGION_NAME = os.environ.get("AWS_REGION", "eu-west-1")
AWS_SES_REGION_ENDPOINT = os.environ.get("EMAIL_HOST")
OPENSEARCH_KEY = os.environ.get("OPENSEARCH_KEY")
OPENSEARCH_SECRET = os.environ.get("OPENSEARCH_SECRET")
OPENSEARCH_ENDPOINT = os.environ.get("OPENSEARCH_ENDPOINT")

USE_S3 = eval(os.environ.get("USE_S3", "0")) in TRUE

if USE_S3 is True:
    INSTALLED_APPS = INSTALLED_APPS + ["storages", "wagtail_storages"]

    # AWS_LOCATION = "static"

    STATICFILES_STORAGE = "storages.backends.s3.S3Storage"
    DEFAULT_FILE_STORAGE = "storages.backends.s3.S3Storage"

    AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STATIC_BUCKET_NAME", "")
    AWS_S3_CUSTOM_DOMAIN = os.getenv("AWS_S3_CUSTOM_DOMAIN")
    AWS_S3_REGION_NAME = "eu-west-1"


WAGTAIL_SITE_NAME = "cib.ie"

BASE_URL = os.environ.get("BASE_URL", "http://localhost:8000")

WAGTAIL_I18N_ENABLED = True

PREFIX_DEFAULT_LANGUAGE = True

WAGTAILADMIN_COMMENTS_ENABLED = False
WAGTAIL_MODERATION_ENABLED = False
WAGTAILIMAGES_IMAGE_MODEL = "cib_images.CustomImage"
WAGTAILIMAGES_FEATURE_DETECTION_ENABLED = False
WAGTAILDOCS_DOCUMENT_MODEL = "cib_documents.CustomDocument"


if OPENSEARCH_KEY and OPENSEARCH_SECRET and OPENSEARCH_ENDPOINT != 'CHANGE':
    from elasticsearch import RequestsHttpConnection
    from requests_aws4auth import AWS4Auth

    WAGTAILSEARCH_BACKENDS = {
        'default': {
            'BACKEND': 'wagtail.search.backends.elasticsearch7',
            'INDEX': 'wagtail',
            'TIMEOUT': 30,
            'HOSTS': [{
                'host': OPENSEARCH_ENDPOINT,
                'port': 443,
                'use_ssl': True,
                'verify_certs': True,
                'http_auth': AWS4Auth(OPENSEARCH_KEY, OPENSEARCH_SECRET, 'eu-west-1', 'es'),
            }],
            'OPTIONS': {
                'connection_class': RequestsHttpConnection,
            },
            'INDEX_SETTINGS': {
                'settings': {
                    'index': {
                        'number_of_shards': 1,
                    },
                    'analysis': {
                        'analyzer': {
                            'default': {
                                'type': 'italian'
                            }
                        }
                    },
                    "max_ngram_diff": "50",
                }
                }

        }
    }
else:
    WAGTAILSEARCH_BACKENDS = {"default": {"BACKEND": "wagtail.search.backends.database"}}

# Default size of the pagination used on the front-end.
DEFAULT_PER_PAGE = 10
DEFAULT_PER_NEWS_PAGE = 12
DEFAULT_PER_DOCUMENT_PAGE = 3

# WAGTAIL_EXPERIMENTAL_FEATURES = ['slim-sidebar']


# cib app

AUTH_USER_MODEL = "cib_users.User"

ROOT_MODEL_CLASS = "cib_home.HomePage"

# wagtailmedia
# https://github.com/torchbox/wagtailmedia
WAGTAILMEDIA = {
    "VIDEO_EXTENSIONS": ["mp4"],  # list of extensions
}

# Recaptcha
# These settings are required for the captcha challange to work.
# https://github.com/springload/wagtail-django-recaptcha

if "RECAPTCHA_PUBLIC_KEY" in os.environ and "RECAPTCHA_PRIVATE_KEY" in os.environ:
    NOCAPTCHA = True
    RECAPTCHA_PUBLIC_KEY = os.environ["RECAPTCHA_PUBLIC_KEY"]
    RECAPTCHA_PRIVATE_KEY = os.environ["RECAPTCHA_PRIVATE_KEY"]
else:
    # To avoid failing github actions
    SILENCED_SYSTEM_CHECKS = ["captcha.recaptcha_test_key_error"]

NOCAPTCHA = True
if USE_CACHE is True:
    SESSION_ENGINE = "django.contrib.sessions.backends.cache"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        # Send logs with at least INFO level to the console.
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "formatters": {
        "verbose": {
            "format": "[%(asctime)s][%(process)d][%(levelname)s][%(name)s] %(message)s"
        }
    },
    "loggers": {
        "cib": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        "wagtail": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        "django.request": {
            "handlers": ["console"],
            "level": "WARNING",
            "propagate": False,
        },
        "django.security": {
            "handlers": ["console"],
            "level": "WARNING",
            "propagate": False,
        },
    },
}
