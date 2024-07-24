import streamlit as st
import streamlit.components.v1 as stc

import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg') # 그림을 표시하는 GUI 창을 열지 않고도 이미지를 생성(서버 환경에서 사용)

import os
from datetime import datetime

from PIL import Image             # 이미지 메타데이터
import exifread                   # 이미지 메타데이터
import mutagen                    # 오디오 메타데이터
from PyPDF2 import PdfFileReader  # PDF 메타데이터

# HTML
metadata_wiki = """
메타데이터는 데이터의 하나 이상의 측면에 대한 정보를 제공하는 데이터로 정의됩니다. 특정 데이터를 더 쉽게 추적하고 작업할 수 있도록 데이터에 대한 기본 정보를 요약하는 데 사용됩니다.
"""

HTML_BANNER = """
    <div style="background-color:tomato;padding:10px;border-radius:10px">
      <h1 style="color:white;text-align:center;">
        MetaData Extractor App 
      </h1>
    </div>
    """

# 이미지 로딩 함수  
@st.cache_data      # 캐시를 사용하여 이미지를 한 번만 로드

def load_image(image_file):
    img = Image.open(image_file)
    return img

def get_readable_time(mytime):
  return datetime.fromtimestamp(mytime).strftime('%Y-%m-%d %H:%M:%S')

# Get Image GeoTags
from PIL.ExifTags import TAGS, GPSTAGS
def get_exif(filename):
  exif = Image.open(filename)._getexif()

  if exif is not None:
    for key, value in exif.items():
      name = TAGS.get(key, key)
      exif[name] = exif.pop(key)

    if 'GPSInfo' in exif:
      for key in exif['GPSInfo'].keys():
        name = GPSTAGS.get(key, key)
        exif['GPSInfo'][name] = exif['GPSInfo'].pop(key)

# 메인 함수
def main(): 
  # st.title("Metadata Extraction App") 
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
      with st.expander("문서 메타데이터 📄📁"):
        st.info("문서 메타데이터")
        st.markdown("📄📁")
        st.text("PDF, Docx 업로드")     
    
  elif choice == "Image":
    st.subheader("Image Metadata Extraction")
    image_file = st.file_uploader("Upload Image", type=['jpg', 'jpeg', 'png', 'gif'])
    if image_file is not None:
      # st.write(type(image_file))
      # st.write(dir(image_file))
      with st.expander("File Stats"):
        file_details = {"FileName":image_file.name, "FileType":image_file.type, "FileSize":image_file.size}
        st.write(file_details)

        statInfo = os.stat(image_file.readable())
        st.write(statInfo)

        stats_details = {"Accessed_Time" : get_readable_time(statInfo.st_atime), 
                         "Creation_Time" : get_readable_time(statInfo.st_ctime), 
                         "Modified_Time" : get_readable_time(statInfo.st_mtime)}
        st.write(stats_details)

        file_details_combined = {"FileName":image_file.name, "FileType":image_file.type, "FileSize":image_file.size,
                                  "Accessed_Time" : get_readable_time(statInfo.st_atime), 
                                  "Creation_Time" : get_readable_time(statInfo.st_ctime), 
                                  "Modified_Time" : get_readable_time(statInfo.st_mtime)}
        # Convert to DataFrame
        df_file_details = pd.DataFrame(list(file_details_combined.items()), columns=['Meta Tags', 'Value'])

        st.dataframe(df_file_details, use_container_width=True)

      # 레이아웃 
      c1, c2 = st.columns(2)
      with c1:
        with st.expander("View Image"):
          img = load_image(image_file)
          st.image(img, width=300, caption="Uploaded Image")
      with c2:
        with st.expander("Default(JPEG)"):
          st.info("Using PILLOW")
          img = load_image(image_file)
          # st.write(dir(img))
          img_details = {"format":img.format, 
                         "mode":img.mode, 
                         "size":img.size, 
                         "format_description":img.format_description
                        }
          # st.write(img_details)

          df_img_details_default = pd.DataFrame(list(img_details.items()), columns=['Meta Tags', 'Value'])
          st.dataframe(df_img_details_default)

      fcol1, fcol2 = st.columns(2)
      with fcol1:
        with st.expander("Exifread Tool"):
          meta_tags = exifread.process_file(image_file)
          # st.write(meta_tags)

          df_img_details_exifread = pd.DataFrame(list(meta_tags.items()), columns=['Meta Tags', 'Value'])
          st.dataframe(df_img_details_exifread)

      with fcol2:
        with st.expander("Image Geo-Coordinates"):
          img_details_with_exif = get_exif(image_file)

          

  elif choice == "Audio":
    st.subheader("Audio Metadata Extraction")

  elif choice == "Document":
    st.subheader("Document Metadata Extraction")

  else:
    st.subheader("About")
    
if __name__ == "__main__":
  main()