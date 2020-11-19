FROM python:3.9.0

WORKDIR /api

RUN apt-get update && apt-get install -y gettext 

RUN pip install --upgrade pip

COPY ./docker/base/requirements.txt ./requirements/base_requirements.txt
COPY ./docker/prod/requirements.txt ./requirements/requirements.txt

RUN pip install -r requirements/requirements.txt

COPY ./src ./src

RUN  rm -rf ./src/config/

COPY ./docker/prod/staff_user/config ./src/config
COPY ./start_server.sh ./start_server.sh

CMD ["/bin/bash", "./start_server.sh"]