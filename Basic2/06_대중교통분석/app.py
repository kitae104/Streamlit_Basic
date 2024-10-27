import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.title("지하철역별 출근 시간대 이용 인원")

# CSV 파일 읽기
df = pd.read_csv("transport.csv", encoding="utf-8")

st.subheader("전체 데이터")
st.dataframe(df)

# Streamlit을 통해 사용자로부터 호선을 입력받기
lines = df.iloc[:, 1].unique()
line = st.selectbox("호선을 입력하세요 : ", lines)  # 호선을 입력받음


# 호선이 입력되면 처리 시작
if line:
    # 첫 번째와 두 번째 줄 제거
    df = df.iloc[1:]

    # 필요한 열 선택 및 데이터 필터링
    filtered_df = df[df.iloc[:, 1] == line]
    st.subheader("호선별 데이터")
    st.dataframe(filtered_df)

    # 역 이름과 합을 저장할 리스트
    name_list = []
    sum_list = []

    for _, row in filtered_df.iterrows():
        row[4:] = row[4:].astype(int)  # 4번째 열부터 끝까지 정수로 변환
        sum_value = row.iloc[[11, 13, 15]].sum()  # 7, 9, 11번째 열의 값 합산
        name_list.append(row[3])  # 역 이름 추가
        sum_list.append(sum_value)  # 합 추가

    # 결과 출력    
    # st.write("역 이름:", name_list)
    # st.write("합:", sum_list)

    # 그래프 출력
    plt.rc('font', family='Malgun Gothic')
    plt.figure(figsize=(12, 6))
    plt.bar(name_list, sum_list, color="blue")
    plt.title(line + "의 하차 인원 ")
    plt.xlabel("역 이름")
    plt.ylabel("인원 수")
    plt.xticks(rotation=90)
    st.pyplot(plt)
