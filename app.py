from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from tensorflow.keras.models import load_model
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import uvicorn
import yfinance as yf
import logging
from time import time



# Inicializa o app FastAPI
app = FastAPI(title="LSTM Stock Predictor")

# Carrega o modelo
model = load_model("lstm_model_aapl.h5")

# Scaler usado no treino
scaler = MinMaxScaler(feature_range=(0, 1))

# Define o formato esperado de entrada
class PriceData(BaseModel):
    prices: list[float]  # últimos 60 preços

@app.get("/")
def home():
    return {"message": "API de Previsão de Ações com LSTM está rodando."}

@app.post("/predict")
def predict_next_price(data: PriceData):
    if len(data.prices) != 60:
        raise HTTPException(status_code=400, detail="É necessário fornecer exatamente 60 valores.")

    # Converte a lista para array e normaliza
    input_data = np.array(data.prices).reshape(-1, 1)
    scaled_data = scaler.fit_transform(input_data)  # normalização com novo scaler

    # Reshape para o LSTM
    X_input = np.reshape(scaled_data, (1, 60, 1))

    # Previsão
    prediction_scaled = model.predict(X_input)
    
    # Reverte normalização com os mesmos dados usados no fit
    prediction_real = scaler.inverse_transform(prediction_scaled)

    return {"next_day_prediction": round(float(prediction_real[0][0]), 2)}

@app.get("/ultimos-precos")
def ultimos_precos():
    try:
        # Baixar os últimos 6 meses de dados
        df = yf.download("AAPL", period="6mo")
        
        # Garante que a coluna 'Close' exista e converte para lista
        if 'Close' not in df.columns:
            raise HTTPException(status_code=500, detail="Coluna 'Close' não encontrada no DataFrame.")
        
        # Pegando os últimos 60 preços da coluna 'Close' como lista
        ultimos_60 = df['Close'].dropna().tail(60).values.tolist()

        if len(ultimos_60) < 60:
            raise HTTPException(status_code=400, detail="Menos de 60 valores disponíveis.")

        return {"prices": ultimos_60}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Configura o logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("lstm-api")

@app.middleware("http")
async def log_requests(request, call_next):
    start_time = time()
    response = await call_next(request)
    duration = round(time() - start_time, 3)
    logger.info(f"{request.method} {request.url.path} - {response.status_code} - {duration}s")
    return response

