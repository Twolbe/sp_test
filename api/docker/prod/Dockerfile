FROM python:3.9.0

WORKDIR /api

RUN apt-get update && apt-get install -y gettext 

RUN pip install --upgrade pip

COPY ./docker/base/requirements.txt ./requirements/base_requirements.txt
COPY ./docker/prod/requirements.txt ./requirements/requirements.txt

RUN pip install -r requirements/requirements.txt
RUN rm -rf ./requirements

COPY . .

CMD ["/bin/bash", "./start_server.sh"]