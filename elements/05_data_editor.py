# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd

@st.cache_data    # 캐시 사용
def load_data():
  # parse_dates: 날짜형식으로 변환 
  df = pd.read_csv("../data/profile.csv", parse_dates=["birthdate"]).dropna() # 결측치 제거
  return df

def main():
  st.title("Data Editor 사용하기")
  df = load_data()
  st.data_editor(df)
  
if __name__ == '__main__':
  main()
  