# Imports

import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from sklearn.cluster import Birch, KMeans
from sklearn.decomposition import PCA
from sklearn.mixture import GaussianMixture

# Get Data

dim_G_x = pd.read_csv("upload_data/dim_G.csv").drop(columns=['weighted_mean', 'iso_a3', 'ind_G5']).dropna().set_index('name')
all_dim_x = pd.read_csv("upload_data/full_df.csv").drop(columns=['weighted_mean', 'iso', 'country-code']).dropna().set_index('name')

# Function Definition


def pca_and_clustering(df_of_indicators, model_choice = "Birch", num_of_clusters = 5):
    
    pca = PCA(n_components=2)

    principalComponents = pca.fit_transform(df_of_indicators.values)
    
    principalDf = pd.DataFrame(data = principalComponents,\
                               columns = ['principal component 1', 'principal component 2'],\
                               index = df_of_indicators.index).reset_index()
    
    X = principalDf.drop(columns=['name']).values
    
    if model_choice == "Birch":
        model = Birch(n_clusters=num_of_clusters)
    if model_choice == "KMeans":
        model = KMeans(n_clusters=num_of_clusters)
    if model_choice == "GaussianMixture":
        model = GaussianMixture(n_components=num_of_clusters)
        
    model.fit(X)
    yhat = model.predict(X)
    
    principalDf = pd.concat([pd.DataFrame(yhat, columns=['Cluster']), principalDf], axis=1)
    principalDf['Cluster'] = principalDf['Cluster'].astype(str)
    
    fig = px.scatter(principalDf,
                 x='principal component 1',
                 y='principal component 2',
                 hover_name='name',
                 color = 'Cluster',
                 title='Scatter plot of Principal Components')

    fig.update_traces(marker=dict(size=10), selector=dict(mode='markers'))  

    return fig






st.title("PCA Dashboard")

n_components = st.slider("Number of Components", min_value=2, max_value=10, value=2)

model_type = st.selectbox("Type of Model", ["Model A", "Model B", "Model C"])

data_set = st.selectbox("Data", ["All Dimensions", "Dimension G"])

if data_set == "All Dimensions":
    data_2_use = all_dim_x
if data_set == "Dimension G":
    data_2_use = dim_G_x


st.plotly_chart(pca_and_clustering(
    df_of_indicators = data_set,
    model_choice= model_type,
    num_of_clusters=n_components))