# -*- coding: utf-8 -*-
# tabs와 columns 사용하기 
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
  
def main():
  st.title("Tabs와 Columns 사용하기")
  day = st.selectbox('Select a day', ['Thur', 'Fri', 'Sat', 'Sun'])
    
  tips = sns.load_dataset('tips')
  filtered_tips = tips[tips['day'] == day]
  top_bill = filtered_tips['total_bill'].max()
  top_tip = filtered_tips['tip'].max()
  
  col1, col2, col3 = st.columns([1, 1, 1]) # 1:2 비율로 컬럼 생성
  with col1:
    st.metric('Tob Buill', f"${top_bill:.2f}")
  with col2:
    st.metric('Top Tip', f"${top_tip:.2f}")
  with col3:
    st.metric('Total Tips', f"${filtered_tips['tip'].sum():.2f}")
  
  tab1, tab2, tab3 = st.tabs(['Total Bill', 'Tip', 'Size'])
  
  with tab1:
    fig, ax = plt.subplots()
    st.header('Total Bill Amounts')
    sns.histplot(filtered_tips['total_bill'], kde=True, ax=ax)
    st.pyplot(fig)
    
  with tab2:
    fig, ax = plt.subplots()
    st.header('Tip Amounts')
    sns.histplot(filtered_tips['tip'], kde=True, ax=ax)
    st.pyplot(fig)
    
  with tab3:
    fig, ax = plt.subplots()
    st.header('Table Sizes')
    sns.boxplot(data=filtered_tips, x='sex', y='tip', ax=ax)
    st.pyplot(fig)
    
  
  
if __name__ == '__main__':
  main() 

