import streamlit as st
import pandas as pd

# ✅ Video Background (Anime Style)
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
        width: auto;
        height: auto;
        z-index: -1;
        object-fit: cover;
        opacity: 0.6;
    }

    .block-container {
        position: relative;
        z-index: 1;
    }
    </style>

    <video autoplay muted loop id="bgvideo">
        <source src="https://videos.pexels.com/video-files/856331/856331-hd_1280_720_25fps.mp4" type="video/mp4">
    </video>
""", unsafe_allow_html=True)

# ✅ Your existing UI
st.title("📊 Student Performance Dashboard")
st.markdown("📁 **Upload StudentsPerformance.csv file**")

uploaded_file = st.file_uploader("Drag and drop file here", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ Dataset uploaded successfully!")
    st.write(df.head())
else:
    st.warning("📂 Please upload the dataset to continue.")
