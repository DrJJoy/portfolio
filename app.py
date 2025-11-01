import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="HLE Predictor", layout="wide")
st.title("Healthy Life Expectancy Predictor")
st.markdown("**PhD in School Psychology | Doctoral Minor in Applied Statistics**")
st.markdown("**20+ Years Building Predictive Models | Python Pipeline**")

df = pd.read_csv("WHR_2025_df2.csv")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("R²", "0.358")
with col2:
    st.metric("Social Support → HLE", "+0.37 years")
with col3:
    st.metric("p-value", "< 0.001")

st.markdown("### Interactive: Social Support vs. HLE")
country = st.selectbox("Filter by Country", ["All"] + sorted(df["Country name"].unique()))
df_plot = df if country == "All" else df[df["Country name"] == country]

fig = px.scatter(
    df_plot,
    x="Explained by: Social support",
    y="Explained by: Healthy life expectancy",
    hover_data=["Country name"],
    trendline="ols",
    title="Social Support Drives Healthy Life Expectancy"
)
st.plotly_chart(fig, use_container_width=True)

st.download_button(
    "Download Full Analysis",
    data=open("model.ipynb", "rb").read(),
    file_name="HLE_Analysis.ipynb",
    mime="application/x-ipynb+json"
)