import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px


st.title("PCA Dashboard")


n_components = st.slider("Number of Components", min_value=2, max_value=10, value=2)

model_type = st.selectbox("Type of Model", ["Model A", "Model B", "Model C"])


st.write(f"This many: {n_components}")
st.write(f"This model: {model_type}")
