# 기본 패키지 
import streamlit as st

# 문자열 입력
fname = st.text_input('이름을 입력하세요', '홍길동', max_chars=10)
st.title(fname)

# 비밀번호 입력
password = st.text_input('비밀번호를 입력하세요', type='password')
st.write(password)


# 문자열 입력
message = st.text_area('메세지를 입력하세요', '메세지를 입력하세요', max_chars=100, height=100)
st.write(message)

# 숫자 입력
number = st.number_input('숫자를 입력하세요', min_value=0, max_value=100, value=50)
st.write(number)

# 날짜 입력
myappointment = st.date_input('예약일을 입력하세요')
st.write(myappointment)

# 시간 입력
mytime = st.time_input('시간을 입력하세요')
st.write(mytime)

# 색상표
color = st.color_picker('색상을 선택하세요')
st.write(color)