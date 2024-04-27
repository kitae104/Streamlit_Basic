# -*- coding:utf-8 -*-
import streamlit as st					# streamlit 모듈 import
from utils import dec_temp              # utlis.py의 내용 import
from eda import run_eda_app				# eda.py의 run_eda_app() 함수 import
from ml import run_ml_app				# ml.py의 run_ml_app() 함수 import


def main():						# 메인 페이지 함수 생성
    st.subheader("Kitae's ML Project")			# 페이지 SubHeader 생성    

    menu = ['HOME', 'EDA', 'ML', 'About']		# 메뉴에 들어갈 목록 작성
    choice = st.sidebar.selectbox("Menu", menu)		# 사이드 바에 SelectBox 생성

    if choice == 'HOME':				# HOME 페이지
        st.subheader('HOME')
        st.markdown(dec_temp, unsafe_allow_html=True)		# HOME 탭에 내용 적용

    elif choice == 'EDA':				# EDA 페이지        
        run_eda_app()					# EDA 페이지 실행
        pass
    elif choice == 'ML':				# ML 페이지
        st.subheader('머신러닝(ML)')
        run_ml_app()
    else:						# ABOUT 페이지
        st.subheader('About')


if __name__ == "__main__":				# 메인 페이지 실행
    main()