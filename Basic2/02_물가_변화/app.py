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

    # 품목 리스트 생성
    food_items = df['품목별'].tolist()
    selected_items = st.multiselect("확인하고 싶은 품목을 선택하세요", options=food_items, default=food_items)

    # 그래프 그리기
    if selected_items:
        plt.rc('font', family='Malgun Gothic')  # 한글 폰트 설정
        plt.figure(figsize=(10, 6))

        for food in selected_items:
            # 선택된 품목에 대한 데이터 필터링
            price = df[df['품목별'] == food].values[0][1:]  # 품목별 열 제외
            price = [0 if item == '-' else float(item) for item in price]  # '-'을 0으로 변환
            years = list(range(2003, 2003 + len(price)))  # 데이터 기간 추정
            years = [str(year) for year in years]

            # 그래프 추가
            plt.plot(years, price, label=food)

        # 그래프 세부 설정
        plt.xlabel('연도')
        plt.ylabel('물가지수')
        plt.xticks(rotation=45)
        plt.title('선택한 간식의 가격 변화')
        plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1), fontsize='small')
        plt.tight_layout()

        # Streamlit에 그래프 표시
        st.pyplot(plt)
    else:
        st.write("선택한 품목이 없습니다. 품목을 선택해주세요.")
