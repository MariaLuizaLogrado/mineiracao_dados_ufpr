import streamlit as st
import plotly.express as px


def plot_map(ano_selecionado, continente_selecionado, variavel_selecionada, df, limites_continentes, tipo_projecao='natural earth'):
    '''
    Função para plotar um mapa interativo com Plotly Express.
    
    Args:
        ano_selecionado (int): Ano selecionado pelo usuário.
        continente_selecionado (str): Continente selecionado pelo usuário.
        df (pd.DataFrame): DataFrame com os dados.
        limites_continentes (dict): Dicionário com os limites geográficos aproximados para os continentes.

    Returns:
        Plotly Express Map: Mapa interativo.
    '''

    # Filtra o DataFrame pelo ano
    df_filtrado = df[df['ano'] == ano_selecionado]

    legenda = variavel_selecionada.replace('_', ' ').title() # Ajusta a legenda
    
    # Criando o mapa com Plotly
    fig = px.choropleth(df_filtrado, 
                        locations='pais',  
                        locationmode='country names',  
                        color=variavel_selecionada,  
                        hover_name='pais',  
                        color_continuous_scale='blues',
                        title=f'{legenda} por País em {ano_selecionado} - {continente_selecionado}')

    # Ajustando o tamanho do mapa
    fig.update_layout(width=1800, height=700)

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
        fig.update_geos(projection_type=tipo_projecao)

    # Exibir o gráfico na página
    st.plotly_chart(fig)