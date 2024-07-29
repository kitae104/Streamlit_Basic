# -*- coding:utf-8 -*-
import streamlit as st 
import pandas as pd 

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
import seaborn as sns
import plotly.express as px

@st.cache_data    # 캐시를 사용하여 데이터를 한 번만 로드
def load_data(data):
    df = pd.read_csv(data)
    return df

def run_eda_app():
    st.subheader("EDA 화면입니다.")
    df = load_data("data/diabetes_data_upload.csv")
    df_encoded = load_data("data/diabetes_data_upload_clean.csv")
    # st.dataframe(df)

    submenu = st.sidebar.selectbox("Submenu", ["Descriptive", "Plots"])
    if submenu == "Descriptive":
        st.dataframe(df) 

        with st.expander("Data Type"):
            st.dataframe(df.dtypes)

        with st.expander("Descriptive Summary"):
            st.dataframe(df_encoded.describe())

        with st.expander("Class Distribution"):
            st.dataframe(df['class'].value_counts())

        with st.expander("Gender Distribution"):
            st.dataframe(df['Gender'].value_counts())

    elif submenu == "Plots":
        pass