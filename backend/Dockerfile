FROM python:3.9.18-slim
    
# Atualizar dependências
RUN apt-get update && apt-get install bash && apt-get install nano -y

# Instalar as dependências
RUN python3 -m pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r ./requirements.txt

# Configurar o diretório de trabalho
WORKDIR /usr/src/app

# Copiar os arquivos necessários para o diretório de trabalho
COPY . .

# Expor a porta 80 para a aplicação FastAPI
EXPOSE 8000

# Comando para executar a aplicação
CMD python3 main.py
