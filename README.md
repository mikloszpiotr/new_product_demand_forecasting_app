
# 📦 New Product Demand Forecasting App

## 💡 Business Problem

Forecasting demand for new products is a persistent challenge for supply chain, demand planning, and commercial teams. New product launches often lack historical sales data, making traditional forecasting unreliable. Inaccurate forecasts can lead to:

- Lost sales due to stockouts  
- Excess inventory and higher holding costs  
- Missed revenue targets  
- Poor market signal responsiveness  

## 🎯 Why Solving This is Critical

Industry research shows that poor new product planning contributes to:

✔️ Up to **30% demand planning errors**  
✔️ Increased operational costs  
✔️ Failed product launches  

Improving new product forecast accuracy enhances revenue predictability, optimizes inventory, and strengthens market competitiveness.

## 🤖 ML Solution Overview

This app uses:

✔️ **Transfer Learning** principles — leveraging historical product data and market analogs to predict demand for new launches  
✔️ **Market Signal Correlation** — utilizing social media trends, search volumes, and pricing signals as predictors  
✔️ **Linear Regression Model** — a simple, interpretable ML model that predicts demand based on normalized market indicators  

### How it works:

- The model is trained using historical products that share market characteristics with the new product  
- Market signals for the new product are collected and normalized  
- A Linear Regression model predicts expected demand using these signals  
- The app displays forecasted demand and key performance indicators in an interactive dashboard  

## 📊 App Features

✔️ Streamlit Dashboard with interactive tabs:  
- **Forecast Overview**: Displays predicted demand for the new product  
- **Market Signals Monitoring**: Visualizes trends in social, search, and pricing indicators  
- **Forecast vs Actual Comparison**: Allows tracking forecast performance post-launch  
- **Lost Demand Cost Estimation**: Estimates business impact of inaccurate forecasts  

## 🛠️ Technology Stack

- Python, Streamlit  
- `pandas`, `numpy` for data handling  
- `scikit-learn` for ML modeling  
- `matplotlib` for visualizations  

## 🚀 Project Structure

```
new_product_demand_forecasting_app/
├── app.py                # Main Streamlit app
├── data/                 # Historical, market signal, and product data
├── models/               # Trained ML model
├── pages/                # Modular Streamlit pages
├── utils/                # Preprocessing functions
├── requirements.txt      # Package dependencies
└── README.md             # Project documentation
```
