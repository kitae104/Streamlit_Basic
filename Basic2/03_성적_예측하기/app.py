import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 제목
st.title("공부 시간에 따른 시험 점수")

# 데이터 불러오기 및 열 이름 변경
df = pd.read_csv('score.csv')
st.dataframe(df)

# 열 이름 변경
df.rename(columns={'Hours':'공부 시간', 'Scores':'시험 점수'}, inplace=True)
st.dataframe(df)

# X와 Y 할당
X = df['공부 시간']
Y = df['시험 점수']

# 플롯 생성
plt.plot()
plt.rc('font', family='Malgun Gothic')
plt.plot(X, Y, 'o')
plt.xlabel('공부 시간')
plt.ylabel('시험 점수')
plt.title('공부 시간에 따른 시험 점수')

# Streamlit에 그래프 표시
st.pyplot(plt)