# Marvelous Insurance - Superhero Public Destruction Events Predictor
Machine Learning system and production-ready FastAPI service for predictiong the annual public destruction events for Marvel Superheroes.

## Project overview
Marvelous Insurance provides insurance for Marvel Superheroes
The objectrive of this project was to build a predictive model that predicts:
**Annual Public Destruction Events**

The model is trained using data extracted from XML credit bureau records.

The final solution includes:
- Load data from DuckDB
- Feature enggineering
- EDA - Exploratory Data Analysis
- Train model
- Compare models
- Model evaluation
- PRoduction-ready FastAPI (Swagger)

#Project Structure
```
marvelous-insurance-destruction-predictor/
│
├── notebooks/
│ ├── eda.ipynb
│ ├── train.ipynb
│ └── inference_testing.ipynb
│
├── app/
│ ├── init.py
│ ├── main.py
│ └── schemas.py
│
├── src/
│ ├── init.py
│ ├── data_loader.py
│ ├── feature_engineering.py
│ └── inference.py
│
├── models/
│ ├── Marvelous_prediction_model.joblib (Final model)
│ ├── Marvelous_prediction_model_lr.joblib (Linear regresion)
│ └── Marvelous_prediction_model_rf.joblib (Random Forrest)
│
├── data/
│ └── superhero_events_db.duckdb (Raw data from Credit Bureau)
│
├── requirements.txt
└── README.md
```

## Data Pipeline
### 1. Data Loading
Data is stored in a DuckDB database:

Table: "superheroes"
Column of intrest: "CreditInfo" (XML Format)

### 2. Feature Engineering 
The following features are extracted from  the XML:
- "Credit_score"
- "age"
- "num_superpowers"
- "num_properties"
- "num_credit_cards"
- "total_credit_limit"

The final model only uses:
["Credit_score", "age", "num_properties"] as they had the biggest correlation to annaul_public_destruction_events 

Malformed XML rows were flagged and excluded from training. In this case only one was excluded

### 3. Training of model

## ML Model

Two models were evaluated
- Linear Regression
- Random Forest Regressor

Evaluation method:
- 10-fold cross validation (only 91 superheroes in data set)
- Metrics:
  - Mean Absolute Error (MAE)
  - Root Mean Squared Error (RMSE)

 ### Final model
 **Random Forest Regressor** 
 Random Forest performed better that Linear Regression over the metrics. 

 ## Model Performance
Evaluation on new clients (training):

- **MAE:** ~ 3.65
- **RMSE:** ~ 4.62  

 ## Production API
 A FastAPI application exposes the model for underwriting use
 This can be used by the call center agent.

### Endpoint: POST/ predict
### Request Body (JSON): 
```json
{
  "credit_info_xml": "<XML string from CreditInfo column>"
}
```
### Response
```json
{
  "predicted_destruction_events": 12
}
```
The model automatically:
- Parses XML
- Extracts required features
- Valudates inout
- Reurns a rounded up destruction prediction






