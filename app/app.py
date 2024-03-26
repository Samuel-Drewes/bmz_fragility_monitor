import streamlit as st
import numpy as np
import pandas as pd


full_df = pd.read_csv("upload_data/full_df.csv")
compare_df = pd.read_csv("upload_data/compare_df.csv")

full_df = full_df\
    .rename(columns={'name': 'Country Name', 'weighted_mean': "Total Score"})\
    .drop(columns = ['iso', 'country-code'])\
    .set_index('Country Name')\
    .dropna(thresh=4)


st.title('BMZ Fragility Dashboard')
st.write("""Definitions on TeamNet: 
         https://teamnet.bmz.bund.de/raum/10034/Teamnet%20Datenlabor/03%20Projekte%20des%20Datenlabors/Fragilit%C3%A4t/defining_fragility_indicators.xlsx?d=w98395878e61e44ab9c77e5e0ef1961d6""")


# Create a sidebar for navigation
page = st.sidebar.selectbox('Choose your page', ['Home', 'Visualization 1', 'Visualization 2'])

if page == 'Home':

    st.header('General Fragility Overview')
    st.write('All dimensions considered')
    st.dataframe(data=full_df)

    st.header('OECD Comparison')
    st.write('Compared to OECD States of Fragility 2022')
    st.dataframe(data=compare_df)

elif page == 'Visualization 1':
    st.title('Visualization 1')
    # Code for visualization 1

elif page == 'Visualization 2':
    st.title('Visualization 2')
    # Code for visualization 2




    




