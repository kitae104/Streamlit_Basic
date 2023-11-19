# 기본 패키지
import streamlit as st

# File Processing 패키지
from PIL import Image
import pandas as pd
import pdfplumber  
from PyPDF2 import PdfReader
import docx2txt 

# Load Images 
@st.cache_resource                      # 캐시를 사용하면 빠르게 이미지를 불러올 수 있음
def load_image(image_file):
    img = Image.open(image_file)        # 이미지 파일을 열어줌
    return img                          # 이미지 파일을 리턴해줌

def load_pdf(pdf_file):
    pdfReader = PdfReader(pdf_file) # pdf 파일을 열어줌
    count = len(pdfReader.pages)          # pdf 파일의 페이지 수를 세어줌
    all_page_text = ""                    # 텍스트를 저장할 변수를 만들어줌
    for i in range(count):
        page = pdfReader.pages[i]              # pdf 파일의 페이지를 불러옴
        all_page_text += page.extract_text()   # pdf 파일의 페이지를 텍스트로 변환해줌
    return all_page_text                 # 텍스트를 리턴해줌

def main():
    st.title("File Upload Tutorial")
    menu = ["Home", "Dataset","DocumentFiles", "About"]
    choice = st.sidebar.selectbox("Menu", menu)                 # 사이드바에 메뉴를 만들어줌

    if choice == "Home":
        st.subheader("Home")
        image_file = st.file_uploader("Upload Image", type=['png', 'jpeg', 'jpg'])  # 이미지 파일을 업로드 할 수 있도록 만들어줌
        if image_file is not None:
            # To See Details
            # st.write(type(image_file))                      # <class 'streamlit.uploaded_file_manager.UploadedFile'>
            # Method/Attribute
            # st.write(dir(image_file))
            file_details = {"Filename":image_file.name,
                            "FileType":image_file.type,
                            "FileSize":image_file.size}
            st.write(file_details)                          # 파일의 정보를 보여줌

            st.image(load_image(image_file), width=350)     # 이미지 파일을 불러와서 보여줌

    elif choice == "Dataset":
        st.subheader("Dataset")
        data_file = st.file_uploader("Upload CSV", type=['csv'])  # csv 파일을 업로드 할 수 있도록 만들어줌
        if data_file is not None:
            # st.write(type(data_file))                   # <class 'streamlit.uploaded_file_manager.UploadedFile'>
            file_details = {"Filename":data_file.name,
                            "FileType":data_file.type,
                            "FileSize":data_file.size}
            st.write(file_details)

            df = pd.read_csv(data_file)                 # csv 파일을 불러와서 보여줌
            st.dataframe(df)                            # df를 보여줌

    elif choice == "DocumentFiles":
        st.subheader("DocumentFiles")
        docx_file = st.file_uploader("Upload Document", type=['pdf', 'docx','txt'])  # pdf, docx, txt 파일을 업로드 할 수 있도록 만들어줌
        if st.button("Process"):
            if docx_file is not None:
                file_details = {"Filename":docx_file.name,
                            "FileType":docx_file.type,
                            "FileSize":docx_file.size}
                st.write(file_details)

                if docx_file.type == "text/plain":
                    raw_text = str(docx_file.read(),"utf-8")
                    st.write(raw_text)            # txt 파일을 불러와서 보여줌
                    
                elif docx_file.type == "application/pdf":
                    raw_text = load_pdf(docx_file) # pdf 파일을 불러와서 보여줌
                    st.write(raw_text)

                elif docx_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                    raw_text = docx2txt.process(docx_file)      # docx 파일을 불러와서 보여줌
                    st.write(raw_text)

    else:
        st.subheader("About")

if __name__ == '__main__':
    main()
