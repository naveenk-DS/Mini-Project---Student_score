import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="Student Performance Dashboard", layout="centered")

# Custom CSS for black background
st.markdown("""
    <style>
        .stApp {
            background-color: black;
        }
        h1 {
            color: white;
        }
        .css-18ni7ap {
            background-color: #1e1e1e;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center;'>🎓 Student Performance Dashboard</h1>", unsafe_allow_html=True)

# File uploader
st.markdown("#### 📁 Upload `StudentsPerformance.csv` file")
uploaded_file = st.file_uploader("Drag and drop file here", type=["csv"])

# If uploaded, show basic info
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")
    st.write(df.head())
else:
    st.warning("⚠️ Please upload the dataset to continue.")
