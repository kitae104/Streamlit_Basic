# -*- coding:utf-8 -*-
import streamlit as st
from streamlit_option_menu import option_menu
from home import run_home
from utils import load_data
from eda.eda_home import run_eda

def main():
  
  total_df = load_data()
  
  with st.sidebar:
    selected = option_menu("대시보드 메뉴", ["홈", "탐색적 자료 분석", "부동산 예측"],  # 메뉴 이름, 메뉴 리스트
                              icons=['house', 'file-bar-graph', 'graph-up-arrow'],      # 메뉴 아이콘
                              menu_icon = 'cast',                                       # 메뉴 아이콘
                              default_index=0)                                          # 기본 선택 메뉴 인덱스
    
  if selected == "홈":
    run_home()
  elif selected == "탐색적 자료 분석":
    run_eda(total_df)
  elif selected == "부동산 예측":
    st.title('부동산 예측')



if __name__ == "__main__":
  main()