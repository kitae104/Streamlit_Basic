import streamlit as st
import streamlit.components.v1 as stc

import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg') # 그림을 표시하는 GUI 창을 열지 않고도 이미지를 생성(서버 환경에서 사용)

from PIL import Image
import exifread
import mutagen 
from PyPDF2 import PdfFileReader

# HTML
metadata_wiki = """
메타데이터는 데이터의 하나 이상의 측면에 대한 정보를 제공하는 데이터로 정의됩니다. 특정 데이터를 더 쉽게 추적하고 작업할 수 있도록 데이터에 대한 기본 정보를 요약하는 데 사용됩니다.
"""

HTML_BANNER = """
    <div style="background-color:tomato;padding:10px;border-radius:10px">
    <h1 style="color:white;text-align:center;">MetaData Extractor App </h1>
    </div>
    """

# 이미지 로딩 함수  
st.cache_data      # 캐시를 사용하여 이미지를 한 번만 로드
def load_image(image_file):
    img = Image.open(image_file)
    return img


def main():  
  stc.html(HTML_BANNER)
  
  menu = ["Home", "Image", "Audio", "Document", "About"]
  choice = st.sidebar.selectbox("Menu", menu)
  
  if choice == "Home":
    st.subheader("Home")
    # 이미지
    st.image(load_image("./images/metadata.png"))
    # 설명
    st.write(metadata_wiki)
    # 확장과 컬럼
    col1, col2, col3 = st.columns(3)
    with col1:
      with st.expander("이미지 메타데이터 📷"):
        st.info("이미지 메타데이터")
        st.markdown("📷")
        st.text("JPEG, JPG, PNG, GIF 이미지 업로드")
        
    with col2:
      with st.expander("오디오 메타데이터 🔉"):
        st.info("오디오 메타데이터")
        st.markdown("🔉")
        st.text("Mp3, Ogg 업로드")
        
    with col3:
      with st.expander("문서 메타데이터 📄"):
        st.info("문서 메타데이터")
        st.markdown("📄")
        st.text("PDF, Docx 업로드")
        
    
    
  elif choice == "Image":
    st.subheader("Image Metadata Extraction")
  elif choice == "Audio":
    st.subheader("Audio Metadata Extraction")
  elif choice == "Document":
    st.subheader("Document Metadata Extraction")
  else:
    st.subheader("About")
    
if __name__ == "__main__":
  main()