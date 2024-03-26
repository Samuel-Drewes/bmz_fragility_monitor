import streamlit as st
import numpy as np
import pandas as pd

st.write('Hello world! UPDATE!!!')

st.title('My Application')
 
# Create a tabbed layout
tabs = st.tabs(['Tab 1', 'Tab 2', 'Tab 3'])
 
# Add content to the first tab
with tabs[0]:
    st.header('Tab 1')
    st.write('This is the content of Tab 1.')
 
# Add content to the second tab
with tabs[1]:
    st.header('Tab 2')
    st.write('This is the content of Tab 2.')
 
# Add content to the third tab
with tabs[2]:
    st.header('Tab 3')
    st.write('This is the content of Tab 3.')

full_df = pd.read_csv("upload_data/full_df.csv")

st.dataframe(data=full_df)