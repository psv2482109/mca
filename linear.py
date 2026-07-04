import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

st.set_page_config(page_title="Linear Regression Demo", layout="wide")

st.title("📈 Linear Regression using Streamlit")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset")
    st.write(df)

    columns = df.columns.tolist()

    x_column = st.selectbox("Select Independent Variable (X)", columns)

    y_column = st.selectbox("Select Dependent Variable (Y)", columns)

    if st.button("Train Model"):

        X = df[[x_column]]
        y = df[y_column]

        model = LinearRegression()
        model.fit(X, y)

        predictions = model.predict(X)

        st.success("Model Trained Successfully!")

        st.subheader("Model Parameters")

        st.write(f"Intercept: {model.intercept_:.4f}")
        st.write(f"Coefficient: {model.coef_[0]:.4f}")

        mse = mean_squared_error(y, predictions)
        r2 = r2_score(y, predictions)

        st.write(f"Mean Squared Error: {mse:.4f}")
        st.write(f"R² Score: {r2:.4f}")

        fig, ax = plt.subplots(figsize=(8,5))

        ax.scatter(X, y, color="blue", label="Actual Data")
        ax.plot(X, predictions, color="red", linewidth=2, label="Regression Line")

        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        ax.legend()

        st.pyplot(fig)

        st.subheader("Predict New Value")

        new_value = st.number_input(
            f"Enter {x_column}",
            float(X.min()),
            float(X.max()),
            float(X.mean())
        )

        prediction = model.predict([[new_value]])

        st.success(f"Predicted {y_column}: {prediction[0]:.2f}")

else:
    st.info("Please upload a CSV file.")