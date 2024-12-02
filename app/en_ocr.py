import streamlit as st
from easyocr import Reader
from utils import load_image, process_image, save_text, prepare_download_button

# Pré-carrega os modelos OCR em cache
@st.cache_resource
def load_reader_en():
    """Carrega o modelo EasyOCR para português."""
    return Reader(['en'])



st.title("Text Detection with OCR :mag_right:")

model = load_reader_en()


# Upload da imagem
uploaded_file = st.file_uploader("Send the image", type=['jpg', 'png', 'jpeg'])
if uploaded_file is not None:
    st.image(uploaded_file, caption='Image sent', use_column_width=True)

    image = load_image(uploaded_file)

    # Botão para detectar texto
    st.write("##### :point_down: Click the button below to detect text in the image")
    if st.button('Detect text'):
        leituras = process_image(image, model)
        st.text_area('Text detect :page_with_curl:', value='\n'.join(leituras), height=200)

        # Salva as leituras em um arquivo
        file_path = save_text(leituras, uploaded_file.name)

        # Prepara botão de download
        prepare_download_button(file_path, uploaded_file.name)

        # Remove o arquivo após o download
        remove_file(file_path)

