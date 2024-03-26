import streamlit as st
import numpy as np
import pandas as pd


full_df = pd.read_csv("upload_data/full_df.csv")

full_df = full_df\
    .rename(columns={'name': 'Country Name', 'weighted_mean': "Total Score"})\
    .drop(columns = ['iso', 'country-code'])\
    .set_index('Country Name')\
    .dropna(thresh=4)


st.title('BMZ Fragility Dashboard')
st.write("Why is this failing?")


# Create a sidebar for navigation
page = st.sidebar.selectbox('Choose your page', ['Home', 'Visualization 1', 'Visualization 2'])

if page == 'Home':
    st.title('General Fragility Overview')
    st.write('All dimensions considered')

    st.dataframe(data=full_df)

elif page == 'Visualization 1':
    st.title('Visualization 1')
    # Code for visualization 1

elif page == 'Visualization 2':
    st.title('Visualization 2')
    # Code for visualization 2




    




