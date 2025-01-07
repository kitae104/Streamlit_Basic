import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv('data/new_bike.csv')
x = df.drop(['Rented Bike Count'], axis=1)
y = df['Rented Bike Count'].values

regr = RandomForestRegressor()
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
regr.fit(x_train, y_train)

def main():
    st.sidebar.header("입력 기반으로 자전거 대여량 예측하기")
    st.sidebar.text("이 앱은 사용자가 입력한 값을 기반으로 자전거 대여량을 예측합니다.")
    st.sidebar.header("아래쪽에 정보를 입력해주세요.")
    st.sidebar.text("Random Forest Regressor를 사용하여 예측합니다.")

    input = 1
    hour = st.slider("시간을 선택해주세요", 0, 23)
    temperature = st.slider("온도를 입력해주세요", -25, 25)
    humidity = st.slider("습도를 입력해주세요", 0, 100)
    wind_speed = st.slider("풍속을 입력해주세요", 0.0, 7.4)
    position = st.slider("가시성을 입력해주세요", 27, 2000)
    dew = st.slider("이슬점을 입력해주세요", -36.6, 27.2)
    solar = st.slider("일사량을 입력해주세요", 0.0, 3.52)
    rainfall = st.slider("강수량을 입력해주세요", 0, 35)
    snowfall = st.slider("적설량을 입력해주세요", 0.0, 8.8)
    seasons = st.slider("계절을 선택해주세요(봄(0), 여름(1), 가을(2), 겨울(3))",0, 3)
    holiday = st.slider("휴일 여부를 선택해주세요(평일(0), 주말(1))",0, 1)
    functioningday = st.slider("근무일 여부을 선택해주세요(근무일(0), 휴일(1))",0, 1)

    inputs = [[hour, temperature, humidity, wind_speed, position, dew, solar, rainfall, snowfall, seasons, holiday, functioningday]]

    if st.button("예측하기"):
        result = regr.predict(inputs)
        st.write("예측된 자전거 대여량은 다음과 같습니다.")
        st.write(result)
        updated_res = result.flatten().astype(float)
        st.write(updated_res)

if __name__ == '__main__':
    main()