# -*- coding: utf-8 -*-
# 셀렉트 박스 사용하기
import streamlit as st
import pandas as pd
import seaborn as sns

@st.cache_data    # 캐시 사용
def load_data():
  df = sns.load_dataset("iris")
  return df
  
def main():
  st.title("Select Box 다루기")  

  iris = load_data()  
  
  st.markdown("## Row 데이터")
  st.dataframe(iris)
  
  st.markdown("<hr>", unsafe_allow_html=True)   # hr 태그 사용
  st.markdown("## Select")
  val = st.selectbox("1개의 종을 선택하세요", iris['species'].unique())
  # val = st.selectbox("1개의 종을 선택하세요", iris.species.unique())      # 위와 동일한 결과
  st.write("선택한 종:", val)
  st.dataframe(iris.loc[iris['species'] == val, :].reset_index(drop=True))  # 선택한 종의 데이터만 출력
  
  st.markdown("<hr>", unsafe_allow_html=True)   # hr 태그 사용
  st.markdown("## MultiSelect")
  cols = st.multiselect("여러개의 종을 선택하세요", iris.columns)
  st.write("선택된 컬럼:", cols)
  st.dataframe(iris.loc[:, cols].reset_index(drop=True))  # 선택한 종의 데이터만 출력
  

if __name__ == '__main__':
  main() 