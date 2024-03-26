import streamlit as st
import numpy as np
import pandas as pd

st.write('Hello world! Schokolade!!!')


full_df = pd.read_csv("upload_data/full_df.csv")

st.dataframe(data=full_df)