import serial
import matplotlib.pyplot as plt
import numpy as np

# 시리얼 포트 설정
ser = serial.Serial('COM3', 9600)

# 그래프 초기화
plt.ion()
fig, ax = plt.subplots()
line, = ax.plot(np.arange(100), np.zeros(100))
ax.set_xlim(0, 100)
ax.set_ylim(-50, 150)  # y축 범위는 데이터 범위에 맞게 조절
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
        unicode_char = data.decode('utf-8')  # 'ö'
        x_value = ord(unicode_char) 
        # print(x_value)
        # acc_x, acc_y, acc_z = map(float, data.split(','))
        # print(f'X: {acc_x}, Y: {acc_y}, Z: {acc_z}')

       # 데이터 저장 및 그래프 업데이트
        y[:-1] = y[1:]
        y[-1] = x_value

        line.set_ydata(y)
        fig.canvas.draw()
        fig.canvas.flush_events()

        i += 1
        if i == 100:
            i = 0
    except ValueError:
        continue
    except KeyboardInterrupt:
        ser.close()
        break
