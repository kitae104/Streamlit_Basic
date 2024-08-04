# -*- coding:utf-8 -*-
import streamlit as st 
import streamlit.components.v1 as stc 
import pandas as pd
import matplotlib.pyplot as plt

html_temp = """
    <div style="background-color:#3872fb;padding:10px;border-radius:10px">
    <h1 style="color:white;text-align:center;">마이크로비트 데이터 분석하기</h1>
    <h4 style="color:white;text-align:center;">Diabetes </h4>
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

def main():
    st.title("Main App")
    stc.html(html_temp)

    menu = ["Home", "Data Analysis", "Graph", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")   
        # st.write(desc_temp)       
        st.markdown(desc_temp, unsafe_allow_html=True)      
    elif choice == "Data Analysis":
        st.subheader("Data Analysis[데이터 분석]")   
        st.write("파일 불러오기")   
        uploaded_file = st.file_uploader("가속도 센서 데이터 파일을 업로드하세요", type=["csv"], key='1')

        if uploaded_file is not None:
            # 파일 읽기
            df = pd.read_csv(uploaded_file)

            # 데이터 확인
            st.write("데이터 미리보기:")
            st.dataframe(df.head(), use_container_width=True)

            # 컬럼이름 변경
            # DataFrame의 컬럼 이름 변경
            df = df.rename(columns={'Time (seconds)': 'Time'})

            st.write("데이터 미리보기(컬럼 변경 후):")
            st.dataframe(df.head(), use_container_width=True)

           # 데이터 정보
            st.write("데이터 정보:")
            st.write(df.info())

            # 기술통계
            st.write("기술통계:")
            st.write(df.describe())

            # 결측치 확인
            st.write("결측치 확인:")
            st.write(df.isnull().sum())

            # 중복값 확인
            st.write("중복값 확인:")
            st.write(df.duplicated().sum())

            # 컬럼별 유니크한 값 확인
            st.write("컬럼별 유니크한 값 확인:")
            for col in df.columns:
                st.write(f"{col}: {df[col].unique()}")


    elif choice == "Graph":
        st.subheader("Graph[시각화]")
        st.write("파일 불러오기")   
        uploaded_file = st.file_uploader("가속도 센서 데이터 파일을 업로드하세요", type=["csv"], key='2')

        if uploaded_file is not None:
            # 파일 읽기
            df = pd.read_csv(uploaded_file)

            # DataFrame의 컬럼 이름 변경
            df = df.rename(columns={'Time (seconds)': 'Time'})
            
            # 하나의 그래프에 출력
            plt.plot(df['Time'], df['x'], label='x')
            plt.plot(df['Time'], df['y'], label='y')
            plt.plot(df['Time'], df['z'], label='z')
            plt.xlabel('Time')
            plt.ylabel('Data')
            plt.title('Sensor Data')
            plt.legend()
            st.pyplot(plt)

            # 각 축별 그래프
            fig, axs = plt.subplots(3, 1, figsize=(10, 10))
            axs[0].plot(df['Time'], df['x'], label='x축', color='r')
            axs[0].set_xlabel('Time')
            axs[0].set_ylabel('x')
            axs[0].legend()

            axs[1].plot(df['Time'], df['y'], label='y축', color='g')
            axs[1].set_xlabel('Time')
            axs[1].set_ylabel('y')
            axs[1].legend()

            axs[2].plot(df['Time'], df['z'], label='z축', color='b')
            axs[2].set_xlabel('Time')
            axs[2].set_ylabel('z')
            axs[2].legend()
            st.pyplot(fig)
    else:
        st.subheader("About")
        
if __name__ == "__main__":
    main()