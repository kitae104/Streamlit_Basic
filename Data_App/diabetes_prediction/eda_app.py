# -*- coding:utf-8 -*-
import streamlit as st 
import pandas as pd 

def run_eda_app():
    st.subheader("EDA 화면입니다.")
    df = pd.read_csv("data/diabetes_data_upload.csv")
    st.dataframe(df)