# Dockerfile
#define imagem base a ser utilizada
FROM python:3.11.11-slim 

#impede criação de arquivos bytecode
ENV PYTHONDONTWRITEBYTECODE 1
#mensagens de erro e log imediatemente visíveis no terminal
ENV PYTHONUNBUFFERED 1

#Atualiza pacotes e instala novos pacotes
RUN apt-get update && apt-get install -y netcat-openbsd gcc libpq-dev

#Define diretório de trabalho code e qualquer comando será executado em code
WORKDIR /code

#Copia arquivos do diretório local para o diretório code do container
COPY requirements.txt /code/

#Atualiza o pip e instala dependencias python do requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

#Copia todos os arquivos locais para o diretório /code/
COPY . /code/

CMD ["daphne", "sala_furiosa.asgi:application", "--bind", "0.0.0.0", "--port", "8000"]