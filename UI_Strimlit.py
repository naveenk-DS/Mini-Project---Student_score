import streamlit as st
import pandas as pd

# Inject CSS + Video Background
st.markdown("""
    <style>
    .stApp {
        background: transparent;
        position: relative;
    }

    video#bgvideo {
        position: fixed;
        top: 0;
        left: 0;
        min-width: 100vw;
        min-height: 100vh;
        object-fit: cover;
        z-index: -1;
        opacity: 0.8;
    }

    .block-container {
        position: relative;
        z-index: 1;
    }
    </style>

    <video autoplay muted loop id="bgvideo">
        <source src="https://moewalls.com/wp-content/uploads/2023/10/yanami-anna-waving-at-you-makeine-thumb.webm" type="video/webm">
    </video>
""", unsafe_allow_html=True)

# UI Elements
st.title("📊 Student Performance Dashboard")
st.markdown("Upload your **StudentsPerformance.csv** file to begin.")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")
    st.write("### Preview of Dataset:")
    st.dataframe(df.head())
else:
    st.warning("⚠️ Please upload the dataset to continue.")
