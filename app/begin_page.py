import streamlit as st 
import os
from PIL import Image

# Caminho absoluto baseado na localização do script
base_dir = os.path.dirname(os.path.abspath(__file__))

st.header("EasyOCR - Detecção de Texto - Text Detection")

st.write("##### Selecione uma bandeira - Select a flag")

ct = st.container()

ct1, ct2 = ct.columns(2)

br_button = ct1.button("Brasil", use_container_width=True)
image_br_path = os.path.join(base_dir, "config", "br.png")
br_logo = Image.open(image_br_path)
ct1.image(br_logo, width=500)

us_button = ct2.button("United States", use_container_width = True)
image_us_path = os.path.join(base_dir, "config", "us.png")
us_logo = Image.open(image_us_path)
ct2.image(us_logo, width=500)

if br_button:
    st.switch_page("pt_ocr.py")

if us_button:
    st.switch_page("en_ocr.py")
