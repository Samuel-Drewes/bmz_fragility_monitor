import streamlit as st
import numpy as np
import pandas as pd

st.title('My Application')
st.write("Why is this failing?")

full_df = pd.read_csv("upload_data/full_df.csv")

st.dataframe(data=full_df)