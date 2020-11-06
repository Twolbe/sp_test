#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset

cd ./src/

export DJANGO_SETTINGS_MODULE=config.settings

python manage.py migrate --noinput

# if [ $DEBUG -eq 0 ] 
# then
# echo "PROD"
python manage.py collectstatic --noinput
uvicorn config.asgi:application --host 0.0.0.0 --port 8000
# elif [ $DEBUG -eq 1 ] 
# then
# echo "DEV"
# sleep infinity
# fi