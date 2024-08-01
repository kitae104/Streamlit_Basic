import serial
import matplotlib.pyplot as plt
import numpy as np
import time

# 시리얼 포트 설정
ser = serial.Serial('COM3', 9600)

# 그래프 초기화
plt.ion()
fig, ax = plt.subplots()
line, = ax.plot(np.arange(100), np.zeros(100))
ax.set_xlim(0, 100)
ax.set_ylim(-128, 127)  # y축 범위는 데이터 범위에 맞게 조절
ax.set_xlabel('시간')
ax.set_ylabel('데이터 값')
plt.show()

# 데이터 수신 및 그래프 업데이트
x = np.arange(100)
y = np.zeros(100)
i = 0

print('Start reading accelerometer data...')

while True:
    try:
        data = ser.read()
        x_value = int.from_bytes(data, byteorder='big', signed=True)        
        print(x_value)

       # 데이터 저장 및 그래프 업데이트
        y[:-1] = y[1:]
        y[-1] = x_value

        line.set_ydata(y)
        fig.canvas.draw()
        fig.canvas.flush_events()

        # i += 1
        # if i == 100:
        #     i = 0
        
    except ValueError:
        continue
    except KeyboardInterrupt:
        ser.close()
        break
