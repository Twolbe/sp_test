FROM python:3.8.3

WORKDIR /api

RUN apt-get update && apt-get install -y gettext 

RUN pip install --upgrade pip
COPY ./docker ./docker
RUN pip install -r docker/dev/requirements.txt
COPY . .

EXPOSE 8000

CMD ["sleep", "infinity"]
