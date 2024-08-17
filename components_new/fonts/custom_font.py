# -*- coding:utf-8 -*-
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 한글폰트 적용
# 폰트 적용
import os
import matplotlib.font_manager as fm  # 폰트 관련 용도 as fm


with open("app\style.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)


def unique(list):
    x = np.array(list)
    return np.unique(x)


def main():

    fontNames = [f.name for f in fm.fontManager.ttflist]
    fontname = st.selectbox("폰트 선택", unique(fontNames))

    plt.rc("font", family=fontname)
    tips = sns.load_dataset("tips")
    fig, ax = plt.subplots()
    sns.scatterplot(data=tips, x="total_bill", y="tip", hue="day")
    ax.set_title("한글 테스트")
    st.pyplot(fig)

    st.dataframe(tips)


if __name__ == "__main__":
    main()
