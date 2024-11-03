import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 페이지 제목과 아이콘 설정
st.set_page_config(page_title="스트림잇", page_icon=":sunglasses:")

st.title('차트 그리기 1')

df = pd.read_csv('iris.csv')

st.dataframe( df.head() )

# sepal_length 와 sepal_width 의 관계를 차트로 그리시오.
fig = plt.figure()
plt.scatter(data=df, x='sepal_length', y='sepal_width')
plt.title('Sepal Length Vs Width')
plt.xlabel('sepal length')
plt.ylabel('sepla width')
st.pyplot(fig)
