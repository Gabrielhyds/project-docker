# Utilizando a imagem base do Alpine
FROM alpine:latest

# Instalando o Python e dependências
RUN apk update && \
    apk add --no-cache python3

# Criando um diretório
RUN mkdir /app

# Copiando o arquivo main.py para dentro da imagem
COPY main.py /app/

# Defina o diretório de trabalho
WORKDIR /app

# Define o ponto de entrada para o container
ENTRYPOINT ["python3", "main.py"]