import streamlit as st 
from PIL import Image

st.set_page_config(
    page_title = "Home",
    page_icon = "📚",
    layout="wide",

)

begin_page = st.Page("begin_page.py", title = "EasyOCR", default= True)

pt_page = st.Page("pt_ocr.py", title = "Português", default=False)

en_page = st.Page("en_ocr.py", title = "English", default = False)


pg = st.navigation(
    {   
        "Home": [begin_page],
        "OCR": [pt_page, en_page]
    }
)

pg.run()