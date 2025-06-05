# Imagem base
FROM python:3.11-slim


# Define o diretório de trabalho
WORKDIR /app

# Copia arquivos para dentro do container
COPY requirements.txt .
COPY app.py .
COPY lstm_model_aapl.h5 .

# Instala as dependências
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expõe a porta da API
EXPOSE 8000

# Comando para iniciar a API
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
