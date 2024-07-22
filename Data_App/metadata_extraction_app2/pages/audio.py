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
    <div style="background-color:#FF8000;padding:10px;border-radius:10px">
    <h1 style="color:white;text-align:center;">Audio MetaData Extractor</h1>
    </div> 
    """


def main():
  # st.title("Metadata Extraction App")
  stc.html(HTML_BANNER)  
 
  
  
    
if __name__ == "__main__":
  main()