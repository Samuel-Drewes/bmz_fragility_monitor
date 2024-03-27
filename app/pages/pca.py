import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px


st.title("PCA Dashboard")


n_components = st.slider("Number of Components", min_value=2, max_value=10, value=2)

model_type = st.selectbox("Type of Model", ["Model A", "Model B", "Model C"])


print(n_components)
print(model_type)
