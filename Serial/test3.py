import streamlit as st
import plotly.graph_objects as go
import time

# Streamlit 앱 시작
st.title("마이크로비트 데이터 실시간 시각화")

# 그래프 초기화
fig = go.Figure(data=go.Scatter(x=[], y=[]))
fig.update_layout(title="실시간 데이터", xaxis_title="시간", yaxis_title="데이터 값")
st.plotly_chart(fig, use_container_width=True)

# 마이크로비트에서 데이터 수신 (예시: 시뮬레이션)
def get_data():
    # 실제로는 마이크로비트와 통신하여 데이터를 받아와야 합니다.
    # 여기서는 임의의 데이터를 생성하여 시뮬레이션합니다.
    return time.time(), time.time() * 2

# 데이터 업데이트 및 그래프 갱신
while True:
    x, y = get_data()

    fig.add_trace(go.Scatter(x=[x], y=[y], mode='markers'))
    fig.update_layout(xaxis_range=[x-10, x+10])  # x축 범위 조절
    st.plotly_chart(fig, use_container_width=True)

    time.sleep(1)  # 1초마다 업데이트