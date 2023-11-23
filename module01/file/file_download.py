# 파일 다운로드 처리 
import streamlit as st
import streamlit.components.v1 as stc

# Utils
import base64
import time
import pandas as pd

timestr = time.strftime("%Y%m%d-%H%M%S")

# text 다운로드
def text_downloader(raw_text):
  b64 = base64.b64encode(raw_text.encode()).decode()                  # strings <-> bytes conversions
  new_filename = "new_text_file_{}_.txt".format(timestr)              # 파일 이름 생성
  st.markdown("#### Download File ###")                               
  href = f'<a href="data:file/txt;base64,{b64}" download="{new_filename}">Click Here!!</a>'   # 다운로드 링크 생성
  st.markdown(href, unsafe_allow_html=True)                           # 다운로드 링크 출력

# CSV 다운로드
def csv_downloader(data):
  csvfile = data.to_csv(index=False)                                  # csv 파일 생성
  b64 = base64.b64encode(csvfile.encode()).decode()                  # strings <-> bytes conversions
  new_filename = "new_text_file_{}_.csv".format(timestr)              # 파일 이름 생성
  st.markdown("#### Download File ###")                               
  href = f'<a href="data:file/txt;base64,{b64}" download="{new_filename}">Click Here!!</a>'   # 다운로드 링크 생성
  st.markdown(href, unsafe_allow_html=True)                           # 다운로드 링크 출력

# Class
class FileDownloader(object):
  """docstring for FileDownloader
	>>> download = FileDownloader(data,filename,file_ext).download()
	"""
  def __init__(self, data, filename='myfile', file_ext='txt'):
    super(FileDownloader, self).__init__()
    self.data = data
    self.filename = filename
    self.file_ext = file_ext

  def download(self):
    b64 = base64.b64encode(self.data.encode()).decode()                  # strings <-> bytes conversions
    new_filename = f"{self.filename}_{timestr}_.{self.file_ext}"     # 파일 이름 생성
    st.markdown("#### Download File ###")                               
    href = f'<a href="data:file/{self.file_ext};base64,{b64}" download="{new_filename}">Click Here!!</a>'   # 다운로드 링크 생성
    st.markdown(href, unsafe_allow_html=True)                           # 다운로드 링크 출력


def main():
  menu = ["Home", "CSV", "About"]
  choice = st.sidebar.selectbox("Menu", menu)

  if choice == "Home":
    st.subheader("Home")
    my_text = st.text_area("Your Message")

    if st.button("Save"):
      st.write(my_text)
      #text_downloader(my_text)
      download = FileDownloader(my_text).download()
  
  elif choice == "CSV":
    df = pd.read_csv("../data/iris.csv")
    st.dataframe(df) 
    # csv_downloader(df)
    download = FileDownloader(df.to_csv(), file_ext='csv').download()

if __name__ == '__main__':
	main()