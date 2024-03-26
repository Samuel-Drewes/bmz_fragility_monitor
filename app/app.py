import streamlit as st
import numpy as np
import pandas as pd

st.title('My Application')
 
# Create tabs
tab_titles = ['Topic A', 'Topic B', 'Topic C']
tab1, tab2, tab3 = st.tabs(tab_titles)
 
# Add content to each tab
with tab1:
    st.header('Topic A')
    st.write('Topic A content')

    full_df = pd.read_csv("upload_data/full_df.csv")

    st.dataframe(data=full_df)
 
with tab2:
    st.header('Topic B')
    st.write('Topic B content')
 
with tab3:
    st.header('Topic C')
    st.write('Topic C content')

