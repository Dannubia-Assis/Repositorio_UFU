# Baixa a iamgem oficial
FROM python:3.13-slim 

# Cria a pasta onde todo comando executado acontecera nela
WORKDIR /app

# Copia todo o projeto para dentro do conteiner
COPY requirements.txt .

# Instala todas as bibliotecas quando necessário
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Quando o conteiner iniciar executa automaticamente o main.py
CMD [ "python", "main.py"]