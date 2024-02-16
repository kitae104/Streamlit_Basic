# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import seaborn as sns

@st.cache_data    # 캐시 사용
def load_data():
  df = sns.load_dataset("tips")
  return df

def main():
  st.title("st.matric() 다루기")  

  tips = load_data()
  st.table(tips.describe())        # 테이블로 표시 

  tip_max = tips['tip'].max()    # 최대값
  tip_min = tips['tip'].min()    # 최소값

  st.metric(label="Max Tip", value=tip_max, delta=tip_max - tip_min)  # delta: 변화량
  st.metric(label="Min Tip", value=tip_min, delta=tip_min - tip_max)  # delta: 변화량


if __name__ == '__main__':
  main()