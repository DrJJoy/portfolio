import streamlit as st
import pandas as pd

# --- Title & Credentials ---
st.set_page_config(page_title="HLE Predictor", layout="wide")
st.title("Healthy Life Expectancy Predictor")
st.markdown("**PhD | Doctoral Minor in Applied Statistics**")
st.markdown("**20+ Years Building Predictive Models | Python Pipeline**")

# --- Key Metrics ---
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("R²", "0.358")
with col2:
    st.metric("Social Support → HLE", "+0.37 years")
with col3:
    st.metric("p-value", "< 0.001")

# --- Business Insight ---
st.markdown("### Key Finding")
st.markdown("**+1 unit of Social Support = +0.37 years of Healthy Life Expectancy** (p < 0.001)")

# --- Data Preview (Hard-Coded from Your Screenshot) ---
st.markdown("### Data Preview (Top 5 Countries)")
data = {
    "Country name": ["Finland", "Denmark", "Iceland", "Sweden", "Netherlands"],
    "Ladder score": [7.736, 7.521, 7.515, 7.345, 7.306],
    "Explained by: Social support": [1.793, 1.748, 1.840, 1.666, 1.667],
    "Explained by: Healthy life expectancy": [0.824, 0.820, 0.873, 0.899, 0.844],
    "Explained by: Generosity": [0.110, 0.150, 0.201, 0.170, 0.186]
}
df_preview = pd.DataFrame(data)
st.dataframe(df_preview)

# --- Full Model Summary ---
st.markdown("### Full Model Results")
st.markdown("""
- **Predictors**: `Explained by: Social support`, `Explained by: Generosity`  
- **Target**: `Explained by: Healthy life expectancy`  
- **R² = 0.358** | 144 countries  
- **Generosity**: non-significant → flagged for removal  
""")

# --- Download Full Analysis ---
st.download_button(
    "Download Full Analysis (Notebook)",
    data=open("model.ipynb", "rb").read(),
    file_name="HLE_Analysis_Full.ipynb",
    mime="application/x-ipynb+json"
)

# --- Next Steps ---
st.markdown("### Next Steps")
st.markdown("""
- Add GDP, Freedom, Corruption for full model  
- Deploy with interactive scatter in local version  
""")
