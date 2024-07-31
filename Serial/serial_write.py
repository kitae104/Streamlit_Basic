import serial
import time

# 시리얼 포트 설정 (보드레이트는 마이크로비트와 동일하게 맞춰야 함)
ser = serial.Serial('COM3', 9600)

while True:
    # 키보드 입력 받기
    key = input("Enter a key (a, b, c): ")

    # 입력된 키에 따라 문자열 전송
    if key == 'a':
        ser.write("on\n".encode())
    elif key == 'b':
        ser.write("off\n".encode())
    elif key == 'c':
        ser.write("test\n".encode())
    else:
        print("Invalid key")

    # 짧은 지연 (필요에 따라 조절)
    time.sleep(0.5)
