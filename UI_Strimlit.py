import streamlit as st
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Set title
st.title("📊 Students Performance Dashboard")

# Load dataset
df = pd.read_csv("/content/StudentsPerformance.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Create new columns
df['total_score'] = df[['math_score', 'reading_score', 'writing_score']].sum(axis=1)
df['average_score'] = df['total_score'] / 3

# Show data
if st.checkbox("🔍 Show Raw Data"):
    st.dataframe(df)



# Section: ML Prediction
st.subheader("🤖 Predict Average Score (Linear Regression)")

# User input sliders
math = st.slider("Math Score", 0, 100, 70)
reading = st.slider("Reading Score", 0, 100, 70)
writing = st.slider("Writing Score", 0, 100, 70)

# Train model
X = df[['math_score', 'reading_score', 'writing_score']]
y = df['average_score']
model = LinearRegression()
model.fit(X, y)

# Predict
input_data = [[math, reading, writing]]
predicted_avg = model.predict(input_data)[0]
st.success(f"🎯 Predicted Average Score: {predicted_avg:.2f}")

