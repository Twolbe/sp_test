FROM python:3.9.0

WORKDIR /api

RUN apt-get update && apt-get install -y gettext 

RUN pip install --upgrade pip
COPY ./docker ./docker
RUN pip install -r docker/prod/requirements.txt
COPY . .

EXPOSE 8000

CMD ["/bin/bash", "./start_server.sh"]
