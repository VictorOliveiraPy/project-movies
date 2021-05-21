# Imagem base oficial 
FROM python:3.9.1-slim-buster

# set diretorio de trabalho
WORKDIR /usr/src/app

# variaveis de ambient
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#install depedencias
RUN pip install poetry

COPY poetry.lock pyproject.toml ./

RUN poetry export -f requirements.txt --output requirements.txt

RUN pip install -r requirements.txt

# add app
COPY . .
