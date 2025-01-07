import streamlit as st
import csv
import matplotlib.pyplot as plt
import pandas as pd 

def read_data(file_path):
  high = []
  low = []
  with open(file_path, 'rt', encoding='utf-8') as f:
    data = csv.reader(f)
    next(data)
    for row in data:
      if row[-1] != '' and row[-2] != '':
        data = row[0].split('-')
        if 1983 <= int(data[0]):
          if data[1] == '06' and data[2] == '14':
            high.append(float(row[-1]))
            low.append(float(row[-2]))
  return high, low

def plot_graph(high, low):
  plt.figure(figsize=(10, 6))
  plt.plot(high, label="high", color="hotpink")
  plt.plot(low, label="low", color="skyblue")
  plt.title("BirthDay Graph(6/14)")
  plt.xlabel("day")
  plt.ylabel("temp")
  plt.legend()
  plt.grid(True)
  st.set_option('deprecation.showPyplotGlobalUse', False)
  st.pyplot()



# Streamlit 웹앱 타이틀 및 설명
st.title("생일 날의 기온 변화 그래프")
st.write("서울시 과거 데이터를 이용하여 생일날 날씨를 확인해보세요.")

# 데이터 불러오기
# df = pd.read_csv("ML_Model/weather/seoul.csv")
df = pd.read_csv("D:/Github/Streamlit_WS/Streamlit_Basic/ML_Model/weather/seoul.csv")
st.data_editor(df, use_container_width=True)

# 데이터 불러오기
high, low = read_data("seoul.csv")

# 그래프 출력
plot_graph(high, low)
