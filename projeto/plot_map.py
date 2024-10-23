import streamlit as st
import plotly.express as px
def plot_map(ano_selecionado, continente_selecionado, df, limites_continentes):
    # Filtra o DataFrame pelo ano
    df_filtrado = df[df['ano'] == ano_selecionado]
    
    # Criando o mapa com Plotly
    fig = px.choropleth(df_filtrado, 
                        locations='pais',  
                        locationmode='country names',  
                        color='relato_sarampo',  
                        hover_name='pais',  
                        color_continuous_scale='blugrn',  # paleta de cores disponíveis: 'emrld', 'blugrn', 'teal', 'agsunset', 'sunset', 'solar', 'ice', 'gray', 'hot', 'curl'
                        title=f'Relatos de Sarampo por País em {ano_selecionado} - {continente_selecionado}')

    # Ajustando o tamanho do mapa
    fig.update_layout(width=1200, height=900)

    # Se o usuário selecionar um continente específico
    if continente_selecionado != 'Mapa Global':
        # Aplicando zoom baseado nos limites do continente selecionado
        limites = limites_continentes[continente_selecionado]
        fig.update_geos(
            projection_scale=1,  # Tamanho padrão do zoom (ajustável)
            center=dict(lat=(limites['lat'][0] + limites['lat'][1]) / 2, 
                        lon=(limites['lon'][0] + limites['lon'][1]) / 2),
            lonaxis_range=limites['lon'],  # Definindo o intervalo de longitude
            lataxis_range=limites['lat'],  # Definindo o intervalo de latitude
            visible=True
        )
    else:
        # Se "Mapa Global" for selecionado, restaura o mapa global
        fig.update_geos(projection_type='natural earth')

    # Exibir o gráfico na página
    st.plotly_chart(fig)