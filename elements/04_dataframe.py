# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import seaborn as sns

@st.cache_data    # 캐시 사용
def load_data():
  df = sns.load_dataset("iris")
  return df

def main():
  st.title("DataFrame 다루기")
  st.checkbox("Use container width", value=False, key="use_container_width")

  iris = load_data()
  # st.session_state 객체를 사용하여 이전 use_container_width의 값을 가져옴
  st.dataframe(iris, use_container_width=st.session_state.use_container_width) # use_container_width=True로 하면 전체 화면에 표시됨 

  # 판다스 스타일 
  st.dataframe(iris.iloc[:5, 0:3].style.highlight_max(axis=1))  # axis=0: 열별로, axis=1: 행별로


if __name__ == '__main__':
  main()