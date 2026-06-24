import streamlit as st
import pandas as pd

st.title("chai sales dashboard")

file=st.file_uploader("upload you csv file",type=["csv"])

if file:
    df=pd.read_csv(file)
    st.subheader("data preview")
    st.dataframe(df)

if file:
    st.subheader("summary stats")
    st.write(df.describe())

if file:
    cities=df["city"].unique()
    selected_city=st.selectbox("filter by cities",cities)
    filtered_data=df[df["city"]==selected_city]
    st.dataframe(filtered_data)