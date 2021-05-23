# Imagem base oficial 
FROM python:3.9.1-slim-buster

# set diretorio de trabalho
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# variaveis de ambient
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

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

 #copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# add app
COPY . .


# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]