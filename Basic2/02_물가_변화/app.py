import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit 설정
st.title("간식 가격 변화 분석")
st.write("빵, 사탕, 아이스크림, 스낵과자, 주스, 탄산음료, 떡볶이, 치킨, 햄버거, 피자의 가격 변화를 확인할 수 있습니다.")

# CSV 파일 로드
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type="csv")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)
    except FileNotFoundError:
        st.error("CSV 파일을 찾을 수 없습니다. 파일 이름과 경로를 확인해 주세요.")

    # 사용자 입력
    foods = df.loc[:, '품목별']  # 품목별 데이터 추출 
    food = st.selectbox("어떤 간식의 가격 변화를 보고 싶나요?", foods)
    st.write(f"선택한 간식: {food}")


    if True:
        # 데이터 필터링
        price = list(df[df['품목별']==food].values[0])  # 선택한 간식의 가격 데이터 추출
        price = price[1:]  # 품목별 열 제외
        
        # st.write(price) # 가격 데이터 출력
        # price = [float(item) for item in price]  # 문자열을 실수로 변환
        
        price = [0 if item == '-' else float(item) for item in price] # '-'을 0으로 변환 
        years = list(range(2003, 2003 + len(price)))  # 데이터 기간 추정
        years = [str(item) for item in years]

        # 그래프 그리기
        plt.rc('font', family='Malgun Gothic')    
        plt.plot(years, price, label = food)
        plt.xlabel('연도')
        plt.ylabel('물가지수')
        plt.xticks(rotation=45)
        plt.title(food + '의 물가 변화')
        plt.legend()

        # Streamlit에 그래프 표시
        st.pyplot(plt)
    else:
        st.write("선택한 품목의 데이터를 찾을 수 없습니다.")
