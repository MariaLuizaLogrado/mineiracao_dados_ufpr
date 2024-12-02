import streamlit as st
import base64
import os

def image_to_bytes(image_path):
    '''Converte uma imagem em Base64.'''
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

def load_image(uploaded_file):
    """Carrega a imagem enviada pelo usuário."""
    return uploaded_file.read()

def process_image(image, reader):
    """Processa a imagem usando EasyOCR e retorna os textos detectados."""
    result = reader.readtext(image)
    return [detection[1] for detection in result]

def save_text(leituras, file_name):
    """Salva os textos detectados em um arquivo local."""
    file_path = f"{file_name.split('.')[0]}.txt"
    with open(file_path, 'w') as f:
        for item in leituras:
            f.write(f"{item}\n")
    return file_path

def prepare_download_button(file_path, original_name):
    """Prepara o botão de download para o arquivo de texto gerado."""
    with open(file_path, 'r') as f:
        data = f.read()
    
    download_name = f"{original_name.split('.')[0]}.txt"
    st.download_button(label='Download', data=data, file_name=download_name, mime='text/plain')

#função para apagar o arquivo assim que ele for baixado
def remove_file(file_path):
    """Remove o arquivo após o download."""
    os.remove(file_path)
