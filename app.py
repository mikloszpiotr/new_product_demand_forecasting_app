
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import numpy as np

st.title("📦 New Product Demand Forecasting App")

st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Overview", "Market Signals", "Forecast vs Actual", "Lost Demand Cost"])

data = pd.read_csv("data/historical_data.csv")
market = pd.read_csv("data/market_signals.csv")
new_product = pd.read_csv("data/new_product_info.csv")

with open("models/transfer_learning_model.pkl", "rb") as f:
    model = pickle.load(f)

if page == "Overview":
    st.header("Forecast Overview")
    st.write(new_product)

    st.write("**Predicting New Product Demand Using Market Signals:**")
    X_new = new_product[["Market_Signal_Score"]].values
    # Simulate using all three market signals with same value for demo purposes
    X_new_expanded = np.hstack([X_new, X_new, X_new])
    forecast = model.predict(X_new_expanded)[0]

    st.metric(label="Predicted Demand (Units)", value=int(forecast))

elif page == "Market Signals":
    st.header("Market Signals Monitoring")
    st.line_chart(market.set_index("Signal_Date"))

elif page == "Forecast vs Actual":
    st.header("Forecast vs Actual Demand")
    actual = [500, 600, 550, 580]
    forecast = [520, 590, 560, 570]
    df = pd.DataFrame({"Actual": actual, "Forecast": forecast})
    st.line_chart(df)

elif page == "Lost Demand Cost":
    st.header("Lost Demand Cost Estimation")
    lost_cost = [1000, 800, 1200, 1100]
    plt.plot(lost_cost)
    st.pyplot(plt.gcf())
