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
  st.title("Matplotlip 다루기")  

  tips = load_data()
  st.table(tips.describe())        # 테이블로 표시 

  # 데이터 가공 
  m_tips = tips.loc[tips['sex'] == "Male"]
  f_tips = tips.loc[tips['sex'] == "Female"]

  # 시각화 차트
  fig, ax = plt.subplots(ncols=2, figsize=(10, 6), sharey=True, sharex=True)
  ax[0].scatter(m_tips['total_bill'], m_tips['tip'], color="blue")
  ax[0].set_title("남자")
  ax[1].scatter(m_tips['total_bill'], m_tips['tip'], color="red")
  ax[1].set_title("여자")
  st.pyplot(fig)          # plt.show() 대신 사용

if __name__ == '__main__':
  main() 

