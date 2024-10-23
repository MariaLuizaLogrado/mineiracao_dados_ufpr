import streamlit as st
import pandas as pd

from plot_map import plot_map

# Defina o título da página e o ícone

# Defina o ícone como um emoji
st.set_page_config(
    page_title="Visualização Dados OMS",  # Título da página
    page_icon="🌐",  # Ícone de mundo disponível
    layout="wide"  # Layout opcional
)

col1, col2 = st.columns([4, 1])  # A primeira coluna será maior que a segunda

# Na primeira coluna, exibe o texto
with col1:
    st.write("""
    # Visualização dos dados de saúde de forma global
    ##### Disponibilizados pela Organização Mundial da Saúde (OMS)
    ###### https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who/data
    """)

# Na segunda coluna, exibe a logo
with col2:
    st.image('logo_oms.jfif', width=350)

# Carregando o arquivo CSV
df = pd.read_csv('expectativa_vida.csv')
mydf = df[['pais', 'ano', 'continente', 'relato_sarampo', 'expectativa_vida', 'consumo_alcool', 'mortalidade_adulta']]

# Dicionário com limites geográficos aproximados para os continentes
limites_continentes = {
    'South America': {'lon': [-82.5, -32.5], 'lat': [-55.0, 12.5]},
    'Europe': {'lon': [-31.0, 60.0], 'lat': [34.0, 71.0]},
    'Asia': {'lon': [30.0, 180.0], 'lat': [-10.0, 80.0]},
    'North America': {'lon': [-170.0, -30.0], 'lat': [5.0, 85.0]},
    'Africa': {'lon': [-20.0, 55.0], 'lat': [-35.0, 38.0]},
    'Oceania': {'lon': [110.0, 180.0], 'lat': [-50.0, 10.0]}
}

# Configurações do mapa na barra lateral
st.sidebar.markdown('## 🛠️ Configurações do Mapa')

# Seletor de ano
ano_selecionado = st.sidebar.slider(label = 'Ano 📅', min_value=2000, max_value=2015, value=2000, step=1)

# Seletor de variável
variavel_selecionada = st.sidebar.selectbox(label = 'Variável 📊', options = ['expectativa_vida', 'relato_sarampo', 'consumo_alcool', 'mortalidade_adulta'])

# Seletor de continente
continente_selecionado = st.sidebar.selectbox(label = 'Continente 🌍', options = ['Mapa Global', 'South America', 'Europe', 'Asia', 'North America', 'Africa', 'Oceania'])

# Seletor de projeção do mapa
if continente_selecionado == 'Mapa Global':
    tipo_projecao = st.sidebar.selectbox(label = 'Projeção 🗺️', options = ['equirectangular', 'azimuthal equal area', 'satellite', 'natural earth'])
else:
    tipo_projecao = 'equirectangular'

# Chame a função com os valores escolhidos
plot_map(ano_selecionado, continente_selecionado, variavel_selecionada, mydf, limites_continentes, tipo_projecao)