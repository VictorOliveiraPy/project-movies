# Imagem base oficial 
FROM python:3.9.1-slim-buster

# variaveis de ambient
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# set diretorio de trabalho
ADD . /app

WORKDIR /app

# install system dependencies
RUN apt-get update \
  && apt-get -y install gcc postgresql \
  && apt-get clean

#install depedencias
RUN pip install --upgrade pip
RUN pip install poetry

COPY poetry.lock pyproject.toml ./

RUN poetry export -f requirements.txt --output requirements.txt

RUN pip install -r requirements.txt



