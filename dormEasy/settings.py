"""
Django settings for dormEasy project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '################'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost']


# Application definition

INSTALLED_APPS = [
    #Third Party appS#
    'ckeditor',
    'ckeditor_uploader',
    'social_django', #as we have installed social-auth-app-django
    'import_export',
    'multiselectfield', #For Using the ModelMultipleChoiceField for our concerned_hostels columns.
    # Custom apps #
    'complain.apps.ComplainConfig',
    'noticeapp.apps.NoticeappConfig', #App for Handling Notices
    'users.apps.UsersConfig', # App for Handling the Users(e.g. Custom User Model)
    # Pre installed apps #
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
IMPORT_EXPORT_USE_TRANSACTIONS = True #to be on safe side while importing to db
# FOR stroing the ckeditor files:-
CKEDITOR_UPLOAD_PATH = 'ckeditor_uploads/'
CKEDITOR_CONFIGS= {
    'default':{
        'width': 'auto',
    },
}
# AUTH_USER_MODEL = 'users.CustomUser' # Here we have specified to Use the Custom User Model
#                             # for our Website.

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ######FOR Social Login#####
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'dormEasy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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
AUTHENTICATION_BACKENDS = (
                    'social_core.backends.open_id.OpenIdAuth',  # for Google authentication
                    'social_core.backends.google.GoogleOpenId',  # for Google authentication
                    'social_core.backends.google.GoogleOAuth2',  # for Google authentication
                    'social_core.backends.facebook.FacebookOAuth2',
                    'django.contrib.auth.backends.ModelBackend',
                )
SOCIAL_AUTH_FACEBOOK_KEY = '############'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '#################'  # App Secret
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY ='###################'  #Paste CLient Key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '#################' #Paste Secret Key

WSGI_APPLICATION = 'dormEasy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
# LOGIN_REDIRECT_URL = 'homepage'# name of home url # to redirect the user to The Home page 

# LOGIN_URL = 'blogapp-newhome'
LOGIN_REDIRECT_URL = 'users-new-profile'
LOGIN_URL = '/#login'

STATIC_URL = '/static/'
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT= os.path.join(BASE_DIR,'media') # full path to store the uploaded files
MEDIA_URL='/media/'
############ SETTINGS TO CONFIGURE THE EMAIL SENDING PROCEDURE ############
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = '####@gmail.com'
EMAIL_HOST_PASSWORD = '#######'
