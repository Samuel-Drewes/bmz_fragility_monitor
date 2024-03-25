import streamlit as st

st.write('Hello world! UPDATE!!!')

full_df = pd.read_csv("../upload_data/full_df.csv")

st.dataframe(data=full_df)