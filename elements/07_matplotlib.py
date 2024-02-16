# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import seaborn as sns

@st.cache_data    # 캐시 사용
def load_data():
  df = sns.load_dataset("tips")
  return df

def main():
  st.title("Matplotlip1 다루기")  

  tips = load_data()
  st.table(tips.describe())        # 테이블로 표시 


if __name__ == '__main__':
  main() 