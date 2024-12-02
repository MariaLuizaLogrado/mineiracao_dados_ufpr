import streamlit as st 
from PIL import Image


# image = Image.open("config/logo.png")
# st.image(image, width=250)

st.header("EasyOCR - Detecção de Texto - Text Detection")

st.write("##### Selecione uma bandeira - Select a flag")

ct = st.container()

ct1, ct2 = ct.columns(2)

comprador_button = ct1.button("Brasil", use_container_width=True)
comprador_logo = Image.open("./config/br.png")
ct1.image(comprador_logo, width=500)

coord_buton = ct2.button("United States", use_container_width = True)
coord_logo = Image.open("./config/us.png")
ct2.image(coord_logo, width=500)

if comprador_button:
    st.switch_page("pt_ocr.py")

if coord_buton:
    st.switch_page("en_ocr.py")
