import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="HLE Predictor", layout="wide")
st.title("Healthy Life Expectancy Predictor")
st.markdown("**PhD in School Psychology | Doctoral Minor in Applied Statistics**")
st.markdown("**20+ Years Building Predictive Models | Python Pipeline**")

df = pd.read_csv("WHR_2025_df2.csv")

# Key Metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("R²", "0.358")
with col2:
    st.metric("Social Support → HLE", "+0.37 years")
with col3:
    st.metric("p-value", "< 0.001")

# Interactive Scatter
st.markdown("### Interactive: Social Support vs. HLE")
country = st.selectbox("Filter by Country", ["All"] + sorted(df["Country name"].unique()))
df_plot = df if country == "All" else df[df["Country name"] == country]

fig, ax = plt.subplots()
ax.scatter(df_plot["Explained by: Social support"], df_plot["Explained by: Healthy life expectancy"])
ax.set_xlabel("Social Support")
ax.set_ylabel("Healthy Life Expectancy")
ax.set_title("Social Support Drives Healthy Life Expectancy")
st.pyplot(fig)

# Download Notebook
st.download_button(
    "Download Full Analysis",
    data=open("model.ipynb", "rb").read(),
    file_name="HLE_Analysis.ipynb",
    mime="application/x-ipynb+json"
)
