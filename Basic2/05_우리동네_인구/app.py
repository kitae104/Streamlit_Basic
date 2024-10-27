import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.title("우리동네 인구 구조 시각화")

# CSV 파일 읽기
df = pd.read_csv("202409_202409_연령별인구현황_월간.csv")
st.subheader("전체 데이터")
st.dataframe(df)

# Streamlit을 통해 사용자로부터 동 이름을 입력받기
findDong = st.text_input("동 이름을 입력하세요:")
#st.write(findDong)

# 동 이름이 입력되었을 때만 처리
if findDong:
    # 사용자 입력을 포함하는 행을 필터링
    filtered_df = df[df.iloc[:, 0].str.contains(findDong)]
    st.subheader("선택한 동네 데이터")
    st.dataframe(filtered_df)

    # 남성 데이터와 여성 데이터 리스트 생성
    male_data = []
    female_data = []

    # 데이터 추출
    if not filtered_df.empty:
        for _, row in filtered_df.iterrows():
            male_data = [-int(i) for i in row[3:104]]  # 남성 데이터 (음수로 변환)
            female_data = [int(i) for i in row[106:]]  # 여성 데이터

    # 데이터가 없으면 에러 메시지 출력
    if not male_data or not female_data:
        st.write("해당 동에 대한 데이터가 없습니다.")
    else:
        # 결과 출력
        st.write("남성 데이터:", male_data)
        st.write("여성 데이터:", female_data)

        # 그래프 시각화
        plt.rc('font', family='Malgun Gothic')
        plt.rcParams['axes.unicode_minus'] = False
        plt.figure(figsize=(10, 8))
        plt.title(findDong + " 지역의 남녀 성별 인구 분포")
        plt.barh(range(101), male_data, label='남성', color='blue')
        plt.barh(range(101), female_data, label='여성', color='red')
        plt.legend()
        st.pyplot(plt)