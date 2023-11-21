# 기본 패키지
import streamlit as st
import os

# File Processing 패키지
from PIL import Image
import pandas as pd

# Load Images 
@st.cache_resource                      # 캐시를 사용하면 빠르게 이미지를 불러올 수 있음
def load_image(image_file):
    img = Image.open(image_file)        # 이미지 파일을 열어줌
    return img                          # 이미지 파일을 리턴해줌

# Save Image to tempDir
def save_uploaded_file(uploadedfile):
    with open(os.path.join("tempDir", uploadedfile.name), 'wb') as f:
        f.write(uploadedfile.getbuffer())
    return st.success("Saved file :{} in tempDir".format(uploadedfile.name))

def main():
    st.title("File Upload & Saved File to Directory App")
    
    menu = ["Home", "Dataset", "About"]
    choice = st.sidebar.selectbox("Menu", menu)                 # 사이드바에 메뉴를 만들어줌

    if choice == "Home":
        st.subheader("Home")
        image_file = st.file_uploader("Upload Image", type=['png', 'jpeg', 'jpg'])  # 이미지 파일을 업로드 할 수 있도록 만들어줌
        if image_file is not None:            
            file_details = {"Filename":image_file.name,
                            "FileType":image_file.type,
                            "FileSize":image_file.size}
            st.write(file_details)                          # 파일의 정보를 보여줌
            st.image(load_image(image_file), width=350)     # 이미지 파일을 불러와서 보여줌

            # Save Image
            save_uploaded_file(image_file)

    elif choice == "Dataset":
        st.subheader("Dataset")
        data_file = st.file_uploader("Upload CSV", type=['csv'])  # csv 파일을 업로드 할 수 있도록 만들어줌
        if data_file is not None:
            file_details = {"Filename":data_file.name,
                            "FileType":data_file.type,
                            "FileSize":data_file.size}
            st.write(file_details)

            df = pd.read_csv(data_file)                 # csv 파일을 불러와서 보여줌
            st.dataframe(df)                            # df를 보여줌

            # Save CSV
            save_uploaded_file(data_file)

    else:
        st.subheader("About")

if __name__ == '__main__':
    main()
