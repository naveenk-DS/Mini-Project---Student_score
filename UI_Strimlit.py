import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
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

# Section: Visualizations
st.subheader("📈 Visualizations")

# Subject selection
subject = st.selectbox("Choose a subject", ['math_score', 'reading_score', 'writing_score'])

# Histogram plot
fig1, ax1 = plt.subplots()
sns.histplot(df[subject], kde=True, bins=20, ax=ax1)
ax1.set_title(f"{subject.capitalize()} Distribution")
st.pyplot(fig1)

# Boxplot for average scores by gender
fig2, ax2 = plt.subplots()
sns.boxplot(data=df, x='gender', y='average_score', ax=ax2)
ax2.set_title("Average Score by Gender")
st.pyplot(fig2)

# Correlation heatmap
fig3, ax3 = plt.subplots()
sns.heatmap(df[['math_score', 'reading_score', 'writing_score']].corr(), annot=True, cmap="YlGnBu", ax=ax3)
ax3.set_title("Correlation Between Subjects")
st.pyplot(fig3)

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

