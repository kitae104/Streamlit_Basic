import streamlit as st 
import streamlit.components.v1 as stc 
import pandas as pd
import matplotlib.pyplot as plt

html_temp = """
    <div style="background-color:#3872fb;padding:10px;border-radius:10px">
    <h1 style="color:white;text-align:center;">마이크로비트 데이터 분석하기</h1>
    <h4 style="color:white;text-align:center;">Diabetes </h4>
    </div>
    """

desc_temp = """
    ### 제목
    설명 1
    #### 작은 제목1
        설명2
    #### 작은 제목2
        - 설명3
        - 설명4
    """

def main():
    st.title("Main App")
    stc.html(html_temp)

    menu = ["Home", "Data Analysis", "Graph", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")           
        st.markdown(desc_temp, unsafe_allow_html=True)      

    elif choice == "Data Analysis":
        st.subheader("Data Analysis[데이터 분석]")                 


    elif choice == "Graph":
        st.subheader("Graph[시각화]")
        
    else:
        st.subheader("About")
        
if __name__ == "__main__":
    main()