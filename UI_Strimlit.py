import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="📊 Student Dashboard", layout="wide")

st.markdown("""
    <style>
    .stApp {
        position: relative;
        overflow: hidden;
    }

    video {
        position: fixed;
        top: 0;
        left: 0;
        min-width: 100vw;
        min-height: 100vh;
        object-fit: cover;
        z-index: -1;
        opacity: 0.7;
    }

    .block-container {
        position: relative;
        z-index: 1;
    }
    </style>

    <video autoplay muted loop>
        <source src="https://videos.pexels.com/video-files/856331/856331-hd_1280_720_25fps.mp4" type="video/mp4">
    </video>
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
