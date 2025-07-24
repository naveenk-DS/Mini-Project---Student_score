import streamlit as st
import pandas as pd
df = pd.read_csv("/content/StudentsPerformance.csv")

# ---- PAGE SETUP ----
st.set_page_config(page_title="Student Dashboard", layout="wide")

# ---- CUSTOM BACKGROUND VIDEO (HTML) ----
def set_background_video():
    video_url = "https://www.w3schools.com/howto/rain.mp4"  # Or use any hosted MP4
    st.markdown(f"""
        <style>
        .stApp {{
            background: url("{video_url}");
            background-size: cover;
            background-attachment: fixed;
        }}
        .block-container {{
            backdrop-filter: blur(6px);
            background-color: rgba(255, 255, 255, 0.6);
            padding: 2rem;
            border-radius: 12px;
        }}
        </style>
    """, unsafe_allow_html=True)

# Apply background effect
set_background_video()

# ---- MAIN TITLE ----
st.title("📊 Student Performance Dashboard")

# ---- LOAD DATA ----
df = pd.read_csv("/content/StudentsPerformance.csv")
df.columns = df.columns.str.lower().str.replace(" ", "_")

# ---- DATA DISPLAY ----
if st.checkbox("🔍 Show Raw Data"):
    st.dataframe(df)

# ---- METRICS ----
st.subheader("📌 Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Students", df.shape[0])
col2.metric("Avg Math Score", round(df['math_score'].mean(), 2))
col3.metric("Avg Reading Score", round(df['reading_score'].mean(), 2))

# ---- FILTER SECTION ----
st.subheader("🎯 Filter by Gender")
gender_filter = st.selectbox("Select Gender", df['gender'].unique())
filtered_df = df[df['gender'] == gender_filter]

st.write(f"Showing data for **{gender_filter}** students:")
st.dataframe(filtered_df)

# ---- STYLISH FOOTER ----
st.markdown("""
    <hr>
    <center>Made with ❤️ using Streamlit</center>
""", unsafe_allow_html=True)
