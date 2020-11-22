#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset

cd ./src/

export DJANGO_SETTINGS_MODULE=config.settings.prod

python manage.py migrate --noinput

python manage.py collectstatic --noinput
uvicorn config.asgi:application --host 0.0.0.0 --port 8000
