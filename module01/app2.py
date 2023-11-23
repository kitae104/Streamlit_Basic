# 기본 패키지
import streamlit as st                  # streamlit 패키지
import os

# File Processing 패키지
from PIL import Image                   # 이미지 파일을 불러오기 위한 패키지
import pandas as pd                     # 데이터 처리 위한 패키지

# 이미지 파일을 불러오기 위한 함수
@st.cache_resource                      # 캐시를 사용하면 빠르게 이미지를 불러올 수 있음
def load_image(image_file):
    img = Image.open(image_file)        # 이미지 파일을 열어줌
    return img                          # 이미지 파일을 리턴해줌

# tempDir에 파일을 저장하기 위한 함수
def save_uploaded_file(uploadedfile):
    with open(os.path.join("tempDir", uploadedfile.name), 'wb') as f:       # tempDir에 파일을 저장함
        f.write(uploadedfile.getbuffer())                                   # 파일을 저장함
    return st.success("Saved file :{} in tempDir".format(uploadedfile.name))# 파일이 저장되었다는 메시지를 보여줌

# 메인 함수
def main():
    st.title("Multiple File Uploads App")
    
    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)                 # 사이드바에 메뉴를 만들어줌

    if choice == "Home":
        st.subheader("Upload Multiple Images")
        uploadedfiles = st.file_uploader("Upload Multiple Images", 
                            type=['png', 'jpeg', 'jpg'],        # 이미지 파일을 업로드 할 수 있도록 만들어줌
                            accept_multiple_files=True)         # 여러개의 파일을 업로드 할 수 있도록 만들어줌
        if uploadedfiles is not None:
            #st.write(uploadedfiles)                             # 업로드한 파일의 정보를 보여줌
            for imagefile in uploadedfiles:
                st.write(imagefile.name)                          # 파일의 정보를 보여줌
                st.image(load_image(imagefile), width=250)
                
                # Save Image
                save_uploaded_file(imagefile)                     # 업로드한 이미지 파일을 저장함
    
    else:
        st.subheader("About")

if __name__ == '__main__':
    main()
