import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
# import pydeck as pdk

import csv

#Columner på hemsidan
col1, col2 = st.columns(2)
#För att lägga in innehållet i kolumner, använd: 
    # with col1:
        # kod ex; st.tiltle('Här är ett exempel')

#Logga
st.image('logga.innovia.jpeg', width=500)

#Title
st.title('Innovia')

#Markdown
st.markdown(' ### Welcome, University of Gothenburg')

#DATA 
DATA_URL = (
    'KOMP.csv'
)

D_URL = (
    'job2022.csv'
)

#KOMPETENS DATA
@st.cache_data(persist=True)
def load_data(nrows):
    data = pd.read_csv('KOMP.csv', nrows = nrows)
    return data

data = load_data(1000)

original_data = data

#UNDERRUBRIK
st.markdown(" #### Systemvetenskap at *University of Gothenburg* vs *University of Lund*")

#chart = st.bar_chart(data = pd.DataFrame('KOMP.csv'), *, x = 'Universitet', y = 'Python', width = 300, height = 200, use_container_width = True)

chart_data = pd.DataFrame(np.random.randn(20, 3), columns = ["a", "b", "c"])
st.bar_chart(chart_data)


#RUBRIK för raw data
st.markdown(' #### Display raw data:')

#Show raw data, kompetenser 
if st.checkbox('Kompetenser Raw Data'):
    st.subheader('Raw Data')
    st.write(data)

#JOBTECH DATA
@st.cache_data(persist=True)
def load_data(nrows):
    jobtechdata = pd.read_csv('job2022.csv', nrows = nrows)
    return jobtechdata

jobtechdata = load_data(10000)

#Show raw data, jobtech
if st.checkbox('Jobtech Raw Data'):
    st.subheader('Raw Data')
    st.write(jobtechdata)
