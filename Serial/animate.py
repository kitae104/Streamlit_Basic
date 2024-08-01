import streamlit as st
import time
import matplotlib.pyplot as plt
import numpy as np
from collections import deque
import serial

ser = serial.Serial('COM3', 9600)  # COM 포트 번호 확인 필요

fig, ax = plt.subplots()

x = np.arange(0, 100)
y = deque(np.zeros(100), 100)

ax.set_ylim(-50, 150)
line, = ax.plot(x, np.array(y))
the_plot = st.pyplot(plt)

def animate(value):  # update the y values (every 1000ms)  
    line.set_ydata(np.array(y))
    the_plot.pyplot(plt)
    y.append(value) #append y with a random integer between 0 to 100

while True:    
    try:        
      value = ord(ser.read().decode('utf-8'))      
      print(value)
      animate(value)
      time.sleep(0.01)
    except ValueError:
      continue
    except KeyboardInterrupt:
      ser.close()
      break