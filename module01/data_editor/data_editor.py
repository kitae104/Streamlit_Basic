import streamlit as st
import pandas as pd
import time

timestr = time.strftime("%Y%m%d-%H%M%S")    # 현재 시간을 문자열로 반환

def load_data(data):        # 업로드된 파일을 데이터프레임으로 변환
  return pd.read_csv(data)  # csv 파일을 데이터프레임으로 변환

def main():
  st.title("Data Editor")

  menu = ["Home","About"]
  choice = st.sidebar.selectbox("Menu",menu)

  if choice == "Home":
    st.subheader("Home")
    data_file = st.file_uploader("Upload CSV",type=['csv'])  # csv 파일 업로드

    if data_file is not None:       # 파일이 업로드 되면
      df = load_data(data_file)     # 데이터프레임으로 변환
      
      # saving form
      with st.form(key='editor_form'):
        edited_df = st.data_editor(df)    # df에 대한 수정이 이루어짐
        save_button = st.form_submit_button(label='Save Data')   # 저장 버튼
        #st.write(dir(data_file))   # data_file에 대한 정보를 출력

      if save_button:   # 저장 버튼을 누르면
        new_filename = f"{data_file.name}_{timestr}.csv"  # 새로운 파일명을 만들고
        final_df = edited_df.to_csv()   # 수정된 데이터프레임을 csv로 저장
        st.download_button(             # 다운로드 버튼을 만들어서
          label="Download CSV",         # 누르면 
          data=final_df,                # 수정된 데이터프레임을 다운로드
          file_name=new_filename,       # 새로운 파일명으로
          mime="text/csv"               # csv 파일로
        )

  else:
    st.subheader("About")


if __name__ == '__main__':
  main()