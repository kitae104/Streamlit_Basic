# -*- coding:utf-8 -*-
import streamlit as st 
import streamlit.components.v1 as stc 
import pandas as pd
import matplotlib.pyplot as plt
import base64
import time

html_temp = """
    <div style="background-color:#3872fb;padding:10px;border-radius:10px">
    <h1 style="color:white;text-align:center;">센서 데이터 분석하기</h1>
    <h4 style="color:white;text-align:center;">from Phone</h4>
    </div>
    """

desc_temp = """
    ### 제목
    설명 1
    #### 작은 제목1
        설명2
    #### 작은 제목2
        - 설명3
        - 설명4
    """

timestr = time.strftime("%Y%m%d-%H%M%S")

# CSV 다운로드
def csv_downloader(data):
  csvfile = data.to_csv(index=False)                                  # csv 파일 생성
  b64 = base64.b64encode(csvfile.encode()).decode()                  # strings <-> bytes conversions
  new_filename = "file_{}_.csv".format(timestr)              # 파일 이름 생성
  st.markdown("#### Download File ###")                               
  href = f'<a href="data:file/txt;base64,{b64}" download="{new_filename}">Click Here!!</a>'   # 다운로드 링크 생성
  st.markdown(href, unsafe_allow_html=True)                           # 다운로드 링크 출력


def main():
    st.title("Main App")
    stc.html(html_temp)

    menu = ["Home", "Data Analysis", "Graph1", "Graph2", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")   
        st.markdown(desc_temp, unsafe_allow_html=True)      

    elif choice == "Data Analysis":
        st.subheader("Data Analysis[데이터 분석]")   
        st.write("파일 불러오기")   
        uploaded_file = st.file_uploader("데이터 파일을 업로드하세요", type=["csv"], key='1')

        if uploaded_file is not None:
            # 파일 읽기
            df = pd.read_csv(uploaded_file)

            # 데이터 확인
            st.write("데이터 미리보기:")
            st.dataframe(df.head(), use_container_width=True)

            # 컬럼이름 변경
            df = df.rename(columns={'Time (s)': 'Time', 'Linear Acceleration x (m/s^2)': 'X', 'Linear Acceleration y (m/s^2)': 'Y', 'Linear Acceleration z (m/s^2)': 'Z', 'Absolute acceleration (m/s^2)': 'W'})

            st.write("데이터 미리보기(컬럼 변경 후):")
            st.dataframe(df.head(), use_container_width=True)

           # 데이터 크기 조절(950개)
            df = df[:950]      

            csv_downloader(df)
            

    elif choice == "Graph1":
        st.subheader("Graph[시각화]")
        st.write("파일 불러오기")   
        uploaded_file = st.file_uploader("데이터 파일을 업로드하세요", type=["csv"], key='2')

        if uploaded_file is not None:
            # 파일 읽기
            df = pd.read_csv(uploaded_file)
                       
            # 하나의 그래프에 출력
            plt.plot(df['Time'], df['X'], label='x')
            plt.plot(df['Time'], df['Y'], label='y')
            plt.plot(df['Time'], df['Z'], label='z')
            plt.xlabel('Time')
            plt.ylabel('Data')
            plt.title('Sensor Data')
            plt.legend()
            st.pyplot(plt)

            # 각 축별 그래프
            fig, axs = plt.subplots(3, 1, figsize=(10, 10))
            axs[0].plot(df['Time'], df['X'], label='X', color='r')
            axs[0].set_xlabel('Time')
            axs[0].set_ylabel('X')
            axs[0].legend()

            axs[1].plot(df['Time'], df['Y'], label='Y', color='g')
            axs[1].set_xlabel('Time')
            axs[1].set_ylabel('Y')
            axs[1].legend()

            axs[2].plot(df['Time'], df['Z'], label='Z', color='b')
            axs[2].set_xlabel('Time')
            axs[2].set_ylabel('Z')
            axs[2].legend()
            st.pyplot(fig)

    elif choice == "Graph2":
        st.subheader("Graph[시각화]")
        st.write("파일 불러오기1")   
        uploaded_file1 = st.file_uploader("데이터 파일을 업로드하세요", type=["csv"], key='3')
        st.write("파일 불러오기2")   
        uploaded_file2 = st.file_uploader("데이터 파일을 업로드하세요", type=["csv"], key='4')

        if uploaded_file1 is not None and uploaded_file2 is not None:    
            df1 = pd.read_csv(uploaded_file1)
            df2 = pd.read_csv(uploaded_file2)

            plt.figure(figsize=(8, 6))  # 그래프 크기 조절
            plt.scatter(df1['X'], df1['Y'], label='정상', color='blue', s=10)  # 정상 데이터
            plt.scatter(df2['X'], df2['Y'], label='비정상', color='red', s=10)  # 비정상 데이터

            # 축 레이블 및 제목 설정
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.title('Scatter Plot X-Y')

            # 그리드 추가 (선택사항)
            plt.grid(True)
            st.pyplot(plt)

            plt.figure(figsize=(8, 6))  # 그래프 크기 조절
            plt.scatter(df1['X'], df1['Z'], label='정상', color='blue', s=10)  # 정상 데이터
            plt.scatter(df2['X'], df2['Z'], label='비정상', color='red', s=10)  # 비정상 데이터

            # 축 레이블 및 제목 설정
            plt.xlabel('X')
            plt.ylabel('Z')
            plt.title('Scatter Plot X-Z')

            # 그리드 추가 (선택사항)
            plt.grid(True)
            st.pyplot(plt)

            plt.figure(figsize=(8, 6))  # 그래프 크기 조절
            plt.scatter(df1['Z'], df1['Y'], label='정상', color='blue', s=10)  # 정상 데이터
            plt.scatter(df2['Z'], df2['Y'], label='비정상', color='red', s=10)  # 비정상 데이터

            # 축 레이블 및 제목 설정
            plt.xlabel('Z')
            plt.ylabel('Y')
            plt.title('Scatter Plot Z-Y')

            # 그리드 추가 (선택사항)
            plt.grid(True)
            st.pyplot(plt)

    else:
        st.subheader("About")
        
if __name__ == "__main__":
    main()