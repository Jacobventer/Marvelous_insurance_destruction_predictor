#!/usr/bin/env python
# coding: utf-8

from fastapi import FastAPI, HTTPException
from app.schemas import PredictionRequest, PredictionResponse
from src.inference import predict_from_xml

app = FastAPI(title="Marvelous Insurance Destruction Predictor", version="1.0")

@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    try:
        prediction = predict_from_xml(request.credit_info_xml)

        return PredictionResponse(predicted_destruction_events=prediction        )

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

