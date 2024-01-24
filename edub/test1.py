import streamlit as st
import pandas as pd
import joblib

# .pkl 파일 로드 함수
def load_model(file_path):
    model = joblib.load(file_path)
    return model

# Streamlit 앱 설정
st.title("Streamlit 예제: .pkl 파일 로드")

# .pkl 파일 업로드
uploaded_file = st.file_uploader("모델 파일을 업로드하세요 (.pkl)", type="pkl")

# 파일이 업로드된 경우 모델 로드 및 예측
if uploaded_file is not None:
    st.sidebar.info("파일이 성공적으로 업로드되었습니다.")

    # 모델 로드
    model = load_model(uploaded_file)

    # 예제 데이터 생성 또는 사용자 입력을 받아 예측
    st.subheader("예제 데이터 입력")
    example_data=   st.slider("예제 데이터를 입력하세요:", 0, 100, 10)
    #example_data = st.text_input("예제 데이터를 입력하세요:", 10)

    X = [[int(example_data)]]

    # 모델 예측
    prediction = model.predict(X)

    # 결과 출력
    st.subheader("모델 예측 결과")
    st.write(f"모델 예측 결과: {prediction}")