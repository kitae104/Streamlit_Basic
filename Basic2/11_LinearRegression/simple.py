import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

st.title("간단한 선형 회귀 예제")

# 데이터 입력
st.sidebar.header("데이터 입력")
x_values = st.sidebar.text_area("X 값 (쉼표로 구분)", "1, 2, 3, 4, 5")
y_values = st.sidebar.text_area("y 값 (쉼표로 구분)", "2, 4, 5, 4, 5")

if x_values and y_values:
    try:
        X = np.array([float(x) for x in x_values.split(",")]).reshape(-1, 1)
        y = np.array([float(y) for y in y_values.split(",")])

        # 모델 학습
        model = LinearRegression()
        model.fit(X, y)

        # 회귀선 계산
        y_pred = model.predict(X)

        # 결과 표시
        st.write(f"기울기: {model.coef_[0]:.2f}")
        st.write(f"절편: {model.intercept_:.2f}")

        # 그래프 시각화
        fig, ax = plt.subplots()
        ax.scatter(X, y, label="데이터 포인트")
        ax.plot(X, y_pred, color="red", label="회귀선")
        ax.set_xlabel("X")
        ax.set_ylabel("y")
        ax.legend()
        st.pyplot(fig)

        # 예측 값
        input_value = st.slider("예측할 X 값 입력", min_value=1.0, max_value=10.0, value=5.0)
        if input_value:
            prediction = model.predict(np.array([[input_value]]))[0]
            st.write(f"예측된 y 값: {prediction:.2f}")

    except ValueError:
        st.error("올바른 숫자를 입력하세요.")