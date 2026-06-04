import streamlit as st
import pandas as pd

st.title("📊 Dataset Overview")

uploaded_file = st.file_uploader(
    "Upload corporate_ai_adoption_dataset.csv",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Rows", len(df))
    col2.metric("Columns", len(df.columns))
    col3.metric("Countries", df["country"].nunique())
    col4.metric("Industries", df["industry"].nunique())

    st.subheader("Dataset Preview")

    st.dataframe(df.head(20))

    st.subheader("Column Information")

    st.write(df.dtypes)

else:
    st.info("Upload dataset to continue.")
