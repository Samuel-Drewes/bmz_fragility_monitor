import streamlit as st
import numpy as np
import pandas as pd

st.title('My Application')
st.write("Why is this failing?")


# Create a sidebar for navigation
page = st.sidebar.selectbox('Choose your page', ['Home', 'Visualization 1', 'Visualization 2'])

if page == 'Home':
    st.title('Home Page')
    st.write('Welcome to the application!')

elif page == 'Visualization 1':
    st.title('Visualization 1')
    # Code for visualization 1

elif page == 'Visualization 2':
    st.title('Visualization 2')
    # Code for visualization 2



    full_df = pd.read_csv("upload_data/full_df.csv")

    st.dataframe(data=full_df)




