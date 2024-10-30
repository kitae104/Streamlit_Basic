import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("해외 여행지 방문객 수 분석")

# 데이터 로드
df = pd.read_csv('해외여행지.csv')
st.subheader("전체 데이터 확인")
st.dataframe(df)

# 여행지 데이터 전처리
df1 = df.sum(axis=0) # 각 열의 합계 계산
# st.dataframe(df1)
area = df1.index[2:] # 지역명 추출
#st.write(area)

df['시점'] = pd.to_datetime(df['시점'])
df['month'] = df['시점'].dt.month # 월별 데이터 추출
# st.write(df['month'])

st.subheader("월별 여행지 방문객 수")
# 월별 데이터 그룹화
df_month = df.groupby('month').sum(numeric_only=True)
st.dataframe(df_month)
st.dataframe(df_month.iloc[2, 1:]) # 특정 월 데이터만 추출

# Streamlit 앱 구성
st.subheader("월별 인기 해외 여행지 비율")
selected_month = st.selectbox("월을 선택하세요", range(1, 13), format_func=lambda x: f"{x}월")

# 선택한 월에 대한 파이 차트 표시
if selected_month in df_month.index:  
    plt.rc('font', family='D2Coding')      
    plt.pie(df_month.iloc[selected_month, 1:], labels=area, autopct='%.1f%%', pctdistance=0.8)
    plt.title(f"{selected_month}월에 많이 가는 여행지")
    plt.axis('equal')
    st.pyplot(plt)
else:
    st.write(f"{selected_month}월에 대한 데이터가 없습니다.")
