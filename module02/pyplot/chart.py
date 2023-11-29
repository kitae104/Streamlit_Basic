import streamlit as st
import numpy as np
import pandas as pd

# 데이터 시각화 라이브러리
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")   # 서버에서 사용하는 백엔드 설정
import seaborn as sns
import altair as alt

def main():
  st.title("Plotting with st.Pyplot")
  df = pd.read_csv("../../data/iris.csv")
  df2 = pd.read_csv("../../data/lang_data.csv")
  st.dataframe(df2.head())

  # 바 차트 st.bar_chart()
  st.bar_chart(df[["sepal_length", 'petal_length']])

  # 선 차트 st.line_chart()
  lang_list = df2.columns.tolist()
  lang_choices = st.multiselect("Choose lang", lang_list, default="Java")
  new_df = df2[lang_choices]
  st.line_chart(new_df)

  # 영역 차트 st.area_chart()
  st.area_chart(new_df, use_container_width=True)

  # 알테어 차트 st.altair_chart()
  df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c']
  )
  c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
  )
  st.dataframe(df.head())
  st.write(c)

  st.altair_chart(c, use_container_width=True)   # use_container_width=True: 차트를 화면 전체 너비로 표시

if __name__ == "__main__":
  main()