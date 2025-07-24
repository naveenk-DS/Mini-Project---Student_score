!pip install matplotlib seaborn pandas streamlit

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit page setup
st.set_page_config(page_title="Student Performance Dashboard", layout="centered")

# Background image (school image from Unsplash)
st.markdown("""
    <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1571260899304-425eee4c7efc");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
            background-repeat: no-repeat;
            color: white;
        }
        h1, h2, h3, h4, h5, h6, p {
            color: white;
        }
        .css-18ni7ap {
            background-color: rgba(0,0,0,0.6);
        }
        .block-container {
            background-color: rgba(0, 0, 0, 0.7);
            padding: 1rem;
            border-radius: 12px;
        }
    </style>
""", unsafe_allow_html=True)

# App title
st.markdown("<h1 style='text-align: center;'>🎓 Student Performance Dashboard</h1>", unsafe_allow_html=True)

# File uploader
st.markdown("#### 📁 Upload `StudentsPerformance.csv` file")
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")

    # Dataset preview
    st.subheader("🔍 Dataset Preview")
    st.dataframe(df.head())

    # Summary statistics
    st.subheader("📌 Summary Statistics")
    st.dataframe(df.describe(include='all'))

    # Gender distribution
    st.subheader("🎨 Gender Distribution")
    fig1, ax1 = plt.subplots()
    sns.countplot(data=df, x='gender', palette='pastel', ax=ax1)
    st.pyplot(fig1)

    # Test score histograms
    st.subheader("📚 Test Score Distributions")
    col1, col2 = st.columns(2)

    with col1:
        fig2, ax2 = plt.subplots()
        sns.histplot(df['math score'], kde=True, color='skyblue', ax=ax2)
        ax2.set_title("Math Score")
        st.pyplot(fig2)

    with col2:
        fig3, ax3 = plt.subplots()
        sns.histplot(df['reading score'], kde=True, color='lightgreen', ax=ax3)
        ax3.set_title("Reading Score")
        st.pyplot(fig3)

    # Writing score boxplot
    st.subheader("✍️ Writing Score by Test Preparation Course")
    fig4, ax4 = plt.subplots()
    sns.boxplot(x="test preparation course", y="writing score", data=df, palette="Set2", ax=ax4)
    st.pyplot(fig4)

else:
    st.warning("⚠️ Please upload the dataset to begin.")
