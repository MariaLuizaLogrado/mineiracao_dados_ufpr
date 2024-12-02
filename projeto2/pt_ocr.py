import streamlit as st
from easyocr import Reader
from utils import load_image, process_image, save_text, prepare_download_button

# Pré-carrega os modelos OCR em cache
@st.cache_resource
def load_reader_pt():
    """Carrega o modelo EasyOCR para português."""
    return Reader(['pt'])

st.title("Detecção de Texto com OCR :mag_right:")

modelo = load_reader_pt()

# Upload da imagem
uploaded_file = st.file_uploader("Entre com a imagem", type=['jpg', 'png', 'jpeg'])
if uploaded_file is not None:
    st.image(uploaded_file, caption='Imagem enviada', use_column_width=True)

    image = load_image(uploaded_file)

    # Botão para detectar texto
    st.write("##### :point_down: Clique no botão abaixo para detectar o texto na imagem.")
    if st.button('Detectar texto'):
        leituras = process_image(image, modelo)
        st.text_area('Texto detectado :page_with_curl:', value='\n'.join(leituras), height=200)

        # Salva as leituras em um arquivo
        file_path = save_text(leituras, uploaded_file.name)

        # Prepara botão de download
        prepare_download_button(file_path, uploaded_file.name)

        # Remove o arquivo após o download
        remove_file(file_path)

