# -*- coding: utf-8 -*-
# 체크 박스 사용하기
import streamlit as st
import matplotlib.pyplot as plt 
import numpy as np



def main():
  st.title("체크 박스 다루기")  
  x = np.linspace(0, 10, 100)
  y = np.sin(x)
  
  show_plot = st.checkbox("시각화 보여주기")
  
  fig, ax = plt.subplots()
  ax.plot(x, y)
  
  if show_plot:     # 체크 박스 클릭이 된 경우 
    st.pyplot(fig)
  
if __name__ == '__main__':
  main() 

