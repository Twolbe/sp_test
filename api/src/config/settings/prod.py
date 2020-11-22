from .base import *  # noqa


DEBUG = False

MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")
