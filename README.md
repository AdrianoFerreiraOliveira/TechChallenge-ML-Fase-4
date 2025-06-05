# 📈 LSTM Stock Predictor API

Este projeto é um desafio da Fase 4 do Tech Challenge da FIAP, que consiste em desenvolver um modelo preditivo utilizando **LSTM (Long Short-Term Memory)** para prever o valor de fechamento de ações da empresa **Apple (AAPL)**. O modelo é servido via uma **API RESTful com FastAPI** e está preparado para ser deployado com **Docker**.

---

## 🔧 Tecnologias Utilizadas

- Python 3.10
- TensorFlow / Keras
- FastAPI
- Uvicorn
- yfinance
- scikit-learn
- Docker

---

## 📊 Funcionalidades

- Coleta de dados históricos da Apple via Yahoo Finance (`yfinance`)
- Treinamento de modelo LSTM para previsão de preço de fechamento
- API REST com FastAPI para servir o modelo
- Endpoint para gerar automaticamente os últimos 60 valores para teste
- Dockerfile para deploy em ambientes de nuvem

---

## 📁 Estrutura do Projeto

```
lstm-stock-api/
├── app.py                 # API com FastAPI
├── lstm_model_aapl.h5     # Modelo LSTM treinado
├── requirements.txt       # Dependências do projeto
├── Dockerfile             # Dockerfile para build
└── README.md              # Este documento
```

---

## ▶️ Como Executar Localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/lstm-stock-api.git
cd lstm-stock-api
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Inicie a API

```bash
uvicorn app:app --reload
```

Acesse: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧪 Como Usar

### 🔹 `/predict` (POST)

**Entrada**: JSON com exatamente 60 preços de fechamento

```json
{
  "prices": [174.3, 173.9, 175.1, ..., 178.2]
}
```

**Saída**:

```json
{
  "next_day_prediction": 179.64
}
```

---

### 🔹 `/ultimos-precos` (GET)

Retorna os últimos 60 preços da Apple para uso direto no `/predict`.

---

## 🐳 Executando com Docker

### 1. Build da imagem

```bash
docker build -t lstm-stock-api .
```

### 2. Run container

```bash
docker run -d -p 8000:8000 lstm-stock-api
```

Acesse novamente: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🚀 Deploy em Nuvem

Você pode subir a API usando plataformas como:
- [Render](https://render.com)
- Railway, Fly.io, Google Cloud Run, etc.

---

## 📡 Monitoramento e Escalabilidade

### 🔍 Logs e Performance
- Middleware para logar tempo de resposta de cada requisição
- Código HTTP, rota e duração são exibidos via `Uvicorn`

### 📊 Métricas (Opcional)
- Expondo métricas via `/metrics` para integração com Prometheus
- Permite rastrear número de requisições, tempo médio, status codes

### 🐳 Escalabilidade
- Pronto para deploy via Docker

---

## 📹 Demonstração em Vídeo

📽️ 

---

## 👨‍💻 Autor

Desenvolvido por **Adriano Ferreira de Oliveira** – Tech Challenge MLET Fase 4.

---

## 📜 Licença

Este projeto é apenas para fins educacionais no contexto do Tech Challenge da FIAP.
