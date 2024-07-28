import streamlit as st
import streamlit.components.v1 as stc

import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use(
    "Agg"
)  # 그림을 표시하는 GUI 창을 열지 않고도 이미지를 생성(서버 환경에서 사용)

import os
from datetime import datetime
import base64

from PIL import Image  # 이미지 메타데이터
import exifread  # 이미지 메타데이터
import mutagen  # 오디오 메타데이터
from PyPDF2 import PdfFileReader  # PDF 메타데이터

# 시간을 문자열로 변환
import time

timestr = time.strftime("%Y%m%d-%H%M%S")

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
@st.cache_data  # 캐시를 사용하여 이미지를 한 번만 로드
def load_image(image_file):
    img = Image.open(image_file)  # 이미지 파일 읽어오기
    return img


def get_readable_time(mytime):
    return datetime.fromtimestamp(mytime).strftime("%Y-%m-%d %H:%M:%S")


# Get Image GeoTags
from PIL.ExifTags import TAGS, GPSTAGS


def get_exif(filename):
    exif = Image.open(filename)._getexif()  # 이미지 파일에서 정보 가져오기

    if exif is not None:
        for key, value in exif.items():
            name = TAGS.get(key, key)
            exif[name] = exif.pop(key)

        if "GPSInfo" in exif:
            for key in exif["GPSInfo"].keys():
                name = GPSTAGS.get(key, key)
                exif["GPSInfo"][name] = exif["GPSInfo"].pop(key)

    return exif


def get_coordinates(info):
    for key in ["Latitude", "Longitude"]:
        if "GPS" + key in info and "GPS" + key + "Ref" in info:
            e = info["GPS" + key]
            ref = info["GPS" + key + "Ref"]
            info[key] = (
                str(e[0][0] / e[0][1])
                + "°"
                + str(e[1][0] / e[1][1])
                + "′"
                + str(e[2][0] / e[2][1])
                + "″ "
                + ref
            )

        if "Latitude" in info and "Longitude" in info:
            return [info["Latitude"], info["Longitude"]]


def get_decimal_coordinates(info):
    for key in ["Latitude", "Longitude"]:
        if "GPS" + key in info and "GPS" + key + "Ref" in info:
            e = info["GPS" + key]
            ref = info["GPS" + key + "Ref"]
            info[key] = (
                e[0][0] / e[0][1] + e[1][0] / e[1][1] / 60 + e[2][0] / e[2][1] / 3600
            ) * (-1 if ref in ["S", "W"] else 1)

    if "Latitude" in info and "Longitude" in info:
        return [info["Latitude"], info["Longitude"]]


# 데이터프레임을 받아와서 CSV 파일로 다운로드하는 함수
def make_downloadable(data):
    csvfile = data.to_csv(index=False)
    b64 = base64.b64encode(csvfile.encode()).decode()  # b64 인코딩
    st.markdown("### ** Download CSV File ** ")
    new_filename = "metadata_result_{}.csv".format(timestr)
    href = f'<a href="data:file/csv;base64,{b64}" download="{new_filename}">Click Here!</a>'
    st.markdown(href, unsafe_allow_html=True)


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
        image_file = st.file_uploader(
            "Upload Image", type=["jpg", "jpeg", "png", "gif"]
        )
        if image_file is not None:
            # st.write(type(image_file))
            # st.write(dir(image_file))
            with st.expander("File Stats"):
                file_details = {
                    "FileName": image_file.name,
                    "FileType": image_file.type,
                    "FileSize": image_file.size,
                }
                st.write(file_details)

                statInfo = os.stat(image_file.readable())
                st.write(statInfo)

                stats_details = {
                    "Accessed_Time": get_readable_time(statInfo.st_atime),
                    "Creation_Time": get_readable_time(statInfo.st_ctime),
                    "Modified_Time": get_readable_time(statInfo.st_mtime),
                }
                st.write(stats_details)

                file_details_combined = {
                    "FileName": image_file.name,
                    "FileType": image_file.type,
                    "FileSize": image_file.size,
                    "Accessed_Time": get_readable_time(statInfo.st_atime),
                    "Creation_Time": get_readable_time(statInfo.st_ctime),
                    "Modified_Time": get_readable_time(statInfo.st_mtime),
                }
                # Convert to DataFrame
                df_file_details = pd.DataFrame(
                    list(file_details_combined.items()), columns=["Meta Tags", "Value"]
                )

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
                    img_details = {
                        "format": img.format,
                        "mode": img.mode,
                        "size": img.size,
                        "format_description": img.format_description,
                    }
                    # st.write(img_details)

                    df_img_details_default = pd.DataFrame(
                        list(img_details.items()), columns=["Meta Tags", "Value"]
                    )
                    st.dataframe(df_img_details_default)

            fcol1, fcol2 = st.columns(2)
            with fcol1:
                with st.expander("Exifread Tool"):
                    meta_tags = exifread.process_file(image_file)
                    # st.write(meta_tags)

                    df_img_details_exifread = pd.DataFrame(
                        list(meta_tags.items()), columns=["Meta Tags", "Value"]
                    )
                    st.dataframe(df_img_details_exifread)

            with fcol2:
                with st.expander("Image Geo-Coordinates"):
                    img_details_with_exif = get_exif(image_file)
                    try:
                        gpg_info = img_details_with_exif
                    except:
                        gpg_info = "None Found"

                    st.write(gpg_info)
                    # img_coordinates = get_decimal_coordinates(gpg_info)
                    # st.write(img_coordinates)

            with st.expander("Download Results"):
                final_df = pd.concat(
                    [df_file_details, df_img_details_default, df_img_details_exifread],
                    axis=0,
                )
                st.dataframe(final_df)
                make_downloadable(final_df)

    elif choice == "Audio":
        st.subheader("Audio Metadata Extraction")
        # File upload
        audio_file = st.file_uploader("Upload Audio", type=["mp3", "ogg"])

        if audio_file is not None:
            col1, col2 = st.columns(2)

            with col1:
                st.audio(audio_file.read())

            with col2:
                with st.expander("File Stats"):
                    file_details = {
                        "FileName": audio_file.name,
                        "FileType": audio_file.type,
                        "FileSize": audio_file.size,
                    }
                    st.write(file_details)

                    statInfo = os.stat(audio_file.readable())
                    st.write(statInfo)

                    stats_details = {
                        "Accessed_Time": get_readable_time(statInfo.st_atime),
                        "Creation_Time": get_readable_time(statInfo.st_ctime),
                        "Modified_Time": get_readable_time(statInfo.st_mtime),
                    }
                    st.write(stats_details)

                    file_details_combined = {
                        "FileName": audio_file.name,
                        "FileType": audio_file.type,
                        "FileSize": audio_file.size,
                        "Accessed_Time": get_readable_time(statInfo.st_atime),
                        "Creation_Time": get_readable_time(statInfo.st_ctime),
                        "Modified_Time": get_readable_time(statInfo.st_mtime),
                    }
                    # Convert to DataFrame
                    df_file_details = pd.DataFrame(
                        list(file_details_combined.items()),
                        columns=["Meta Tags", "Value"],
                    )
                    st.dataframe(df_file_details)

                #  add_file_details(audio_file.name, audio_file.type, audio_file.size, datetime.now())
            
            
            with st.expander("Metadata with Mutagen"):
                meta_tags = mutagen.File(audio_file)
                # st.write(meta_tags)
                df_audio_details_with_mutagen = pd.DataFrame(list(meta_tags.items()), columns=["Meta Tags","Value"])
                st.dataframe(df_audio_details_with_mutagen)  

            with st.expander("Download Results"):
                final_df = pd.concat(
                    [df_file_details, df_audio_details_with_mutagen],
                    axis=0,
                )
                st.dataframe(final_df)
                make_downloadable(final_df)      

    elif choice == "Document":
        st.subheader("Document Metadata Extraction")

    else:
        st.subheader("About")
        st.info("Built with Streamlit")

if __name__ == "__main__":
    main()
