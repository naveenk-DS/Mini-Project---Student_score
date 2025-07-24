import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="📊 Student Dashboard", layout="black")

# Background video (optional visual)
st.markdown("""
    <style>
    .stApp {
        background: url(https://www.w3schools.com/howto/rain.mp4);
        background-size: cover;
        background-attachment: fixed;
    }
    .block-container {
        backdrop-filter: blur(6px);
        background-color: rgba(255, 255, 255, 0.6);
        padding: 2rem;
        border-radius: 12px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("📊 Student Performance Dashboard")

# Upload file
uploaded_file = st.file_uploader("📁 Upload StudentsPerformance.csv file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df.columns = df.columns.str.lower().str.replace(" ", "_")

    # Show raw data
    if st.checkbox("🔍 Show Raw Data"):
        st.dataframe(df)

    # Metrics
    st.subheader("📌 Key Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Students", df.shape[0])
    col2.metric("Avg Math Score", round(df['math_score'].mean(), 2))
    col3.metric("Avg Reading Score", round(df['reading_score'].mean(), 2))

    # Filter by gender
    st.subheader("🎯 Filter by Gender")
    gender = st.selectbox("Select gender", df['gender'].unique())
    filtered_df = df[df['gender'] == gender]
    st.dataframe(filtered_df)

else:
    st.warning("👈 Please upload the dataset to continue.")
