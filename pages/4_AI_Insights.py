import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 AI Insights")

uploaded_file = st.file_uploader(
    "Upload Dataset",
    type=["csv"],
    key="insights"
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("Investment vs Revenue Impact")

    fig1 = px.scatter(
        df.sample(min(5000, len(df))),
        x="ai_investment_usd",
        y="revenue_impact",
        color="industry",
        title="AI Investment vs Revenue Impact"
    )

    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("AI Maturity Score Distribution")

    fig2 = px.histogram(
        df,
        x="ai_maturity_score",
        nbins=30,
        title="AI Maturity Score"
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Yearly Adoption Trend")

    trend = (
        df.groupby("year")
        ["ai_adoption_level"]
        .mean()
        .reset_index()
    )

    fig3 = px.line(
        trend,
        x="year",
        y="ai_adoption_level",
        markers=True,
        title="AI Adoption Trend"
    )

    st.plotly_chart(fig3, use_container_width=True)

else:
    st.info("Upload dataset.")
