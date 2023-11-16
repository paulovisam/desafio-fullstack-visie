# Use a imagem base Node.js
FROM node:20.9.0-slim as node

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo package.json e package-lock.json para o diretório de trabalho
COPY package*.json ./

# Instale as dependências
RUN npm install

# Copie o restante dos arquivos da aplicação
COPY . .

# Construa a aplicação Angular
RUN npm run build