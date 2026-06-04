import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🌍 Country Analysis")

uploaded_file = st.file_uploader(
    "Upload Dataset",
    type=["csv"],
    key="country"
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    country_avg = (
        df.groupby("country")
        ["ai_adoption_level"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        country_avg,
        x="country",
        y="ai_adoption_level",
        title="Average AI Adoption by Country"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(country_avg)

else:
    st.info("Upload dataset.")
