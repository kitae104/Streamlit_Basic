import streamlit as st
import serial
import matplotlib.pyplot as plt
import numpy as np
import time

# 시리얼 포트 설정
ser = serial.Serial('COM3', 9600)  # COM 포트 번호 확인 필요

# 그래프 초기화
plt.ion()
fig, ax = plt.subplots()
line, = ax.plot(np.arange(100), np.zeros(100))
ax.set_xlim(0, 100)
ax.set_ylim(-50, 150)  # y축 범위는 데이터 범위에 맞게 조절
plt.xlabel('time')
plt.ylabel('value')
# st.pyplot(fig)

# 데이터 수신 및 그래프 업데이트
x = np.arange(100)
y = np.zeros(100)



# Streamlit 앱
def app():
    st.title('마이크로비트 실시간 그래프')
    # 그래프 출력
    st.pyplot(fig)
    i = 0
    # 데이터 수신 및 업데이트
    while True:
        try:
            
            data = ser.read()
            unicode_char = data.decode('utf-8')  # 'ö'
            value = ord(unicode_char)             
            print(value)                    

            y[:-1] = y[1:]
            y[-1] = value        
            
            line.set_ydata(y)

            # 그래프 업데이트가 안됨!!    
            ax.relim()
            ax.autoscale_view()
            fig.canvas.draw_idle()
            
            
        except ValueError:
            continue
        except KeyboardInterrupt:
            ser.close()
            break

if __name__ == '__main__':
    app()