import streamlit as st
import pandas as pd

from plot_map import plot_map

# Defina o título da página e o ícone

# Defina o ícone como um emoji
st.set_page_config(
    page_title="Relatos de Sarampo",  # Título da página
    page_icon="🌐",  # Ícone de mundo disponível
    layout="wide"  # Layout opcional
)

col1, col2 = st.columns([4, 1])  # A primeira coluna será maior que a segunda

# Na primeira coluna, exibe o texto
with col1:
    st.write("""
    # Visualização dos relatos de sarampo em um mapa interativo. 
    ###### Os dados são disponibilizados pela Organização Mundial da Saúde (OMS)
    """)

# Na segunda coluna, exibe a logo
with col2:
    st.image('logo_oms.jfif', width=400)

# Carregando o arquivo CSV
mydf = pd.read_csv('projeto.csv')
df = mydf[['pais', 'ano', 'relato_sarampo', 'continente']]

# Dicionário com limites geográficos aproximados para os continentes
limites_continentes = {
    'South America': {'lon': [-82.5, -32.5], 'lat': [-55.0, 12.5]},
    'Europe': {'lon': [-31.0, 60.0], 'lat': [34.0, 71.0]},
    'Asia': {'lon': [30.0, 180.0], 'lat': [-10.0, 80.0]},
    'North America': {'lon': [-170.0, -30.0], 'lat': [5.0, 85.0]},
    'Africa': {'lon': [-20.0, 55.0], 'lat': [-35.0, 38.0]},
    'Oceania': {'lon': [110.0, 180.0], 'lat': [-50.0, 10.0]}
}

# Seletor de ano
ano_selecionado = st.slider('Selecione um ano', min_value=2000, max_value=2015, value=2000, step=1)

# Seletor de continente
continente_selecionado = st.selectbox('Selecione um continente', ['Mapa Global', 'South America', 'Europe', 'Asia', 'North America', 'Africa', 'Oceania'])

# Chame a função com os valores escolhidos
plot_map(ano_selecionado, continente_selecionado, df, limites_continentes)
