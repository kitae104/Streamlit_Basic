# seaborn 패키지를 사용하여 데이터를 시각화하는 예제
# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache_data    # 캐시 사용
def load_data():
  df = sns.load_dataset("tips")
  return df

def main():
  st.title("Seaborn 다루기")

  tips = load_data()
  st.table(tips.describe())        # 테이블로 표시 

  # 데이터 가공 
  m_tips = tips.loc[tips['sex'] == "Male", :]
  f_tips = tips.loc[tips['sex'] == "Female", :]

  # 시각화 차트
  fig, ax = plt.subplots(ncols=2, figsize=(10, 6), sharey=True, sharex=True)
  sns.scatterplot(data=m_tips, x='total_bill', y='tip', ax=ax[0])
  ax[0].set_title("Male")
  sns.scatterplot(data=f_tips, x='total_bill', y='tip', ax=ax[1])
  ax[0].set(xlabel=None, ylabel=None)
  ax[1].set_title("Femail")
  ax[1].set(xlabel=None, ylabel=None)
  
  st.pyplot(fig)          # plt.show() 대신 사용

if __name__ == '__main__':
  main() 