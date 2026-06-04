import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🏭 Industry Analysis")

uploaded_file = st.file_uploader(
    "Upload Dataset",
    type=["csv"],
    key="industry"
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    industry_avg = (
        df.groupby("industry")
        ["ai_adoption_level"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        industry_avg,
        x="industry",
        y="ai_adoption_level",
        title="Average AI Adoption by Industry"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(industry_avg)

else:
    st.info("Upload dataset.")
