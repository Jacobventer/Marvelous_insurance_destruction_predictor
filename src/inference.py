#!/usr/bin/env python
# coding: utf-8

#Inference Module
import joblib
import pandas as pd
import math
from pathlib import Path
from src.feature_engineering import extract_features_from_xml, MODEL_FEATURES


#Define project root 
BASE_DIR = Path(__file__).resolve().parent         
PROJECT_ROOT = BASE_DIR.parent

MODEL_PATH = PROJECT_ROOT / "models" / "Marvelous_prediction_model.joblib"

model = joblib.load(MODEL_PATH)

#Prediction function
def predict_from_xml(xml_string: str) -> float:
    features = extract_features_from_xml(xml_string)

    if features["xml_parse_error"] == 1:
        raise ValueError("Invalid or malformed XML provided.")

    input_df = pd.DataFrame([features])
    input_df = input_df[MODEL_FEATURES]

    if input_df.isnull().any().any():
        raise ValueError("Missing required values in XML input.")

    prediction = model.predict(input_df)[0]

    #Round up
    rounded_prediction = math.ceil(prediction)

    return int(rounded_prediction)





