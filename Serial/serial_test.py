import streamlit as st
import serial
import time

st.title("Serial Test")

# 시리얼 포트 설정 (보드레이트는 마이크로비트와 동일하게 맞춰야 함)
ser = serial.Serial('COM3', 9600)

# 입력된 키에 따라 문자열 전송
if st.button("LED ON", key='1'):
    ser.write("on\n".encode())
    st.write("LED ON")
    time.sleep(0.5)
if st.button("LED OFF", key='2'):
    ser.write("off\n".encode())
    st.write("LED OFF")
    time.sleep(0.5)
if st.button("TEST", key='3'):
    ser.write("test\n".encode())
    st.write("TEST")
    time.sleep(0.5)
    
