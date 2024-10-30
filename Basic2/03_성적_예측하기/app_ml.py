from sklearn.linear_model import LinearRegression 
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 제목
st.title("공부 시간에 따른 시험 점수 예측하기")

# 데이터 불러오기 및 열 이름 변경
df = pd.read_csv('score.csv')
st.dataframe(df)

# 열 이름 변경
df.rename(columns={'Hours':'공부 시간', 'Scores':'시험 점수'}, inplace=True)
st.dataframe(df)

model = LinearRegression()

X = df[['공부 시간']]
Y = df['시험 점수']

model.fit(X.values, Y)
Y_p = model.predict(X.values)

plt.rc('font', family='D2Coding')
plt.plot(X, Y, 'o')
plt.plot(X, Y_p)
plt.xlabel('공부 시간')
plt.ylabel('시험 점수')
plt.title('공부 시간에 따른 시험 점수 예측선')
st.pyplot(plt)

score = model.score(X.values, Y)
st.write('결정계수: ', score)

study_time = st.number_input('공부 시간을 입력하세요', min_value=0.0, max_value=10.0, step=0.1)
predicted_score = model.predict([[study_time]])
st.write('예측 점수: ', predicted_score[0])

st.write('점수 예측을 위해 공부 시간을 입력하세요')
select_time = st.slider('공부 시간', 0.0, 10.0, 5.0, 0.1)
pred_score = model.predict([[select_time]])
st.write('예측 점수: ', pred_score[0])

import plotly.graph_objects as go

X = df['공부 시간'] 
Y = df['시험 점수']
#Y_p = [예측된 값]  # Y_p는 예측된 점수 값 리스트로, 실제 값을 채워 넣어야 합니다.

# Plotly 산점도 및 예측선 생성
fig = go.Figure()

# 실제 데이터 산점도
fig.add_trace(go.Scatter(x=X, y=Y, mode='markers', name='실제 점수'))

# 예측선
fig.add_trace(go.Scatter(x=X, y=Y_p, mode='lines', name='예측선'))

fig.add_trace(go.Scatter(
    x=[select_time],
    y=[pred_score[0]],
    mode='markers',
    marker=dict(color='red', size=10),
    name='예측 점수'
))

# 그래프 레이아웃 설정
fig.update_layout(
    title='공부 시간에 따른 시험 점수 예측선',
    xaxis_title='공부 시간',
    yaxis_title='시험 점수',
    font=dict(family='D2Coding')  # 폰트 설정
)

# Streamlit에 그래프 표시
st.plotly_chart(fig)