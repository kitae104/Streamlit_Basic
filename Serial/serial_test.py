import streamlit as st
import serial

# 웹 페이지 제목 설정
st.title("Streamlit WebSerial 예제")

# 사용 가능한 시리얼 포트 목록 가져오기
ser = serial.Serial(
    port = 'COM6', 
    baudrate=9600, 
    parity='N',
    stopbits=1,
    bytesize=8,
    timeout=8
    )

#시리얼포트 접속
ser.isOpen()

#시리얼포트 번호 출력
st.write(ser.name)