import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit 앱 제목 설정
st.title('피자와 치킨의 검색지수')

# CSV 파일 업로드
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type="csv")

if uploaded_file is not None:
    # CSV 파일을 pandas로 읽기
    data = pd.read_csv(uploaded_file, encoding='cp949')
    
    st.dataframe(data, use_container_width=True)

    # 날짜, 피자, 치킨 데이터 추출
    date = data.iloc[:, 0]  # 첫 번째 열이 날짜
    pz = data.iloc[:, 1]    # 두 번째 열이 피자 검색 지수
    ck = data.iloc[:, 2]    # 세 번째 열이 치킨 검색 지수
    jb = data.iloc[:, 3]    # 네 번째 열이 족발 검색 지수
    
    # matplotlib 그래프 그리기
    plt.figure(figsize=(10,5))
    plt.rc('font', family='Malgun Gothic')
    plt.plot(date, pz, 'red', label='피자')
    plt.plot(date, ck, 'blue', label='치킨')
    plt.plot(date, jb, 'green', label='족발')
    plt.xticks(rotation=90)
    plt.title('피자와 치킨의 검색지수')
    plt.legend()
    
    # 그래프를 Streamlit에 출력
    st.pyplot(plt)
