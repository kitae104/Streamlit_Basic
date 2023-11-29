import streamlit as st
import numpy as np
import pandas as pd

# 데이터 시각화 라이브러리
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")   # 서버에서 사용하는 백엔드 설정
import seaborn as sns


def main():
  st.title("Plotting with st.Pyplot")
  df = pd.read_csv("../../data/iris.csv")

  st.dataframe(df.head())

  # matplotlib.pyplot으로 그래프 그리기
  fig, ax = plt.subplots()
  ax.scatter(df["sepal_length"], df["sepal_width"])
  st.pyplot(fig)

  # bar chart 그리기 
  fig = plt.figure()
  df['species'].value_counts().plot(kind='bar')
  st.pyplot(fig)

  # seaborn으로 그래프 그리기
  fig = plt.figure()
  sns.countplot(data=df, x="species")
  st.pyplot(fig)

if __name__ == "__main__":
  main()