import streamlit as st                        #En symbolo del sistema se debe poner: python -m streamlit run app.py  Y python -m pip install
import pandas as pd 
import matplotlib.pyplot as plt 

apgn = pd.read_csv('datos_anteproyecto.csv')
ran = pd.read_csv('datos_salario.csv')

st.title("Aplicacion 2")

tab1, tab2 = st.tabs(['Tab 1', 'Tab 2'])

with tab1:
    #analisis univariado
    fig, ax = plt.subplots(1, 3, figsize=(10, 4))
    #educ
    tab_freq = ran['educ'].value_counts().sort_index()
    ax[0].bar(tab_freq.index, tab_freq.values)

    #edad
    ax[1].hist(ran['edad'], bins=30)

    #wage
    ax[2].hist(ran['wage'], bins=30)

    st.pyplot(fig)

    #analisis bivariado
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))

    #educ vs. wage
    ax[0].scatter(ran['educ'], ran['wage'])

    #edad vs. wage
    ax[1].scatter(ran['edad'], ran['wage'])

    st.pyplot(fig)

with tab2:
    fig = px.treemap(data_frame=apgn,
            path=[px.Constant("PGN"),
                  "Nombre Sector",
                  "Tipo de gasto"],
            values='Valor')
    st.plotly_char(fig)

        
