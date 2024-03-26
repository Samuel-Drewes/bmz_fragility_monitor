import streamlit as st
import numpy as np
import pandas as pd
import geopandas as gpd
import plotly.express as px



full_df = pd.read_csv("upload_data/full_df.csv")
compare_df = pd.read_csv("upload_data/compare_df.csv")

clean_df = full_df\
    .rename(columns={'name': 'Country Name', 'weighted_mean': "Total Score"})\
    .drop(columns = ['iso', 'country-code'])\
    .set_index('Country Name')\
    .dropna(thresh=4)

## For the Map

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
geo_merge = world.merge(full_df, left_on = 'iso_a3', right_on = 'iso')

geo_merge = geo_merge.drop(columns=['pop_est', 'continent', 'name_x', 'iso_a3', 'gdp_md_est', 'country-code'])\
    .rename(columns={'name_y': 'Country Name', 'weighted_mean': "Total Score"})\
    .set_index('Country Name')
geo_merge_2 = geo_merge.set_index('Country Name')

red_green_scale = [
    [0, 'red'], 
    [0.5, 'yellow'], 
    [1, 'green']  
]

fig = px.choropleth(geo_merge_2,
                    geojson=geo_merge_2.geometry,
                    locations=geo_merge_2.index,
                    color="Total Score",
                    hover_name=geo_merge_2.index,  # or any column for names
                    hover_data=['Total Score', 'Dimension_G', 'Dimension_S', 'Dimension_S', 'Dimension_I', 'Dimension_C',
       'Dimension_E', 'Dimension_R'],  # Add more columns here
                    projection="mercator",
                    color_continuous_scale=red_green_scale  # Or use 'Plotly3' for a built-in option
                    )
fig.update_geos(fitbounds="locations", visible=False)

# Overall Title

st.title('BMZ Fragility Dashboard')
st.write("""Definitions on TeamNet: 
         https://teamnet.bmz.bund.de/raum/10034/Teamnet%20Datenlabor/03%20Projekte%20des%20Datenlabors/Fragilit%C3%A4t/defining_fragility_indicators.xlsx?d=w98395878e61e44ab9c77e5e0ef1961d6""")



# Sidebar for navigation
page = st.sidebar.selectbox('Choose your page', ['Home', 'Visualization 1', 'Visualization 2'])

if page == 'Home':

    st.header('General Fragility Overview')
    st.write('All dimensions considered')
    st.dataframe(data=clean_df)

    st.header('OECD Comparison')
    st.write('Compared to OECD States of Fragility 2022')
    st.dataframe(data=compare_df)

    st.header('General Fragility Map')
    st.plotly_chart(fig)


elif page == 'Visualization 1':
    st.title('Visualization 1')
    # Code for visualization 1

elif page == 'Visualization 2':
    st.title('Visualization 2')
    # Code for visualization 2




    




