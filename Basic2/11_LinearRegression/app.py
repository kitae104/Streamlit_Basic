import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

st.title("사용자 입력을 활용한 선형 회귀")

# 1단계: 데이터 생성에 대한 사용자 입력
st.sidebar.header("데이터 생성")
n_points = st.sidebar.slider("데이터 포인트 수", min_value=10, max_value=100, value=50)
x_min = st.sidebar.number_input("X 값의 최소값", value=0)
x_max = st.sidebar.number_input("X 값의 최대값", value=10)
y_noise = st.sidebar.slider("노이즈 수준", min_value=0.0, max_value=10.0, value=2.0)

# 데이터 생성
np.random.seed(42)
X = np.random.uniform(x_min, x_max, n_points).reshape(-1, 1)
true_slope = 3.0
true_intercept = 5.0
noise = np.random.normal(0, y_noise, n_points)
y = true_slope * X.flatten() + true_intercept + noise

# 데이터프레임 생성
data = pd.DataFrame({"X": X.flatten(), "y": y})

# 원시 데이터 표시
if st.checkbox("원시 데이터 보기"):
    st.write(data)

# 2단계: 선형 회귀
st.header("선형 회귀")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# 테스트 데이터에 대한 예측
y_pred = model.predict(X_test)

# 모델 계수 표시
st.write("### 모델 계수")
st.write(f"기울기: {model.coef_[0]:.2f}")
st.write(f"절편: {model.intercept_:.2f}")

# 3단계: 시각화
st.header("시각화")
fig, ax = plt.subplots()
ax.scatter(X, y, label="데이터 포인트", alpha=0.6)
ax.plot(X, model.predict(X), color="red", label="회귀선")
ax.set_xlabel("X")
ax.set_ylabel("y")
ax.legend()
st.pyplot(fig)

# 4단계: 스피너를 이용한 예측
st.header("예측")
input_value = st.slider("예측할 X 값 입력", min_value=1.0, max_value=10.0, value=5.0)
with st.spinner("예측 중..."):
    prediction = model.predict(np.array([[input_value]]))[0]
st.success(f"예측된 y 값: {prediction:.2f}")

# 그래프에 예측 결과 표시
fig, ax = plt.subplots()
ax.scatter(X, y, label="데이터 포인트", alpha=0.6)
ax.plot(X, model.predict(X), color="red", label="회귀선")
ax.scatter([input_value], [prediction], color="green", label="예측값", zorder=5)
ax.set_xlabel("X")
ax.set_ylabel("y")
ax.legend()
st.pyplot(fig)
