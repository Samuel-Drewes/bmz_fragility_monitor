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
st.write("""Definitions on TeamNet: 
         https://teamnet.bmz.bund.de/raum/10034/_layouts/15/WopiFrame.aspx?sourcedoc=%7B98395878-E61E-44AB-9C77-E5E0EF1961D6%7D&file=defining_fragility_indicators.xlsx&action=default&IsList=1&ListId=%7B5AB29548-B6D5-46BA-8ED6-1700391C493B%7D&ListItemId=3760""")


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




    




