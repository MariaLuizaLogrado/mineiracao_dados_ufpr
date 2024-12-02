import streamlit as st
from PIL import Image
from utils import image_to_bytes


# Cabeçalho e descrição
st.header("EasyOCR - Detecção de Texto - Text Detection")
st.write("##### Selecione uma bandeira - Select a flag")

# Divisão em colunas
ct1, ct2 = st.columns(2)

# Caminhos para imagens
br_logo_path = "./config/br.png"
us_logo_path = "./config/us.png"

# Geração das imagens em Base64
br_logo_bytes = image_to_bytes(br_logo_path)
us_logo_bytes = image_to_bytes(us_logo_path)

# Criação dos "botões" com HTML personalizado
with ct1:
    st.markdown(
        f"""
        <a href="/pt_ocr" target="_self">
            <img src="data:image/png;base64,{br_logo_bytes}" style="width:100%;cursor:pointer;">
        </a>
        """,
        unsafe_allow_html=True,
    )

with ct2:
    st.markdown(
        f"""
        <a href="/en_ocr" target="_self">
            <img src="data:image/png;base64,{us_logo_bytes}" style="width:100%;cursor:pointer;">
        </a>
        """,
        unsafe_allow_html=True,
    )
