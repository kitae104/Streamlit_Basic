# -*- coding: utf-8 -*-
import streamlit as st

def main():
  st.title("This is Text Elements")
  st.title("한글 처리 확인!")
  st.header("Header")
  st.subheader("Subheader")
  st.write("This is write")
  st.write("-" * 50)
  st.text("This is text")
  
  st.write("-" * 50)
  st.markdown("### This is Markdown")
  st.markdown("""
    ### SubChapter
    - 간단한 수식 : $a^2 + b^2 = c^2$           
  """)
              
  
  
if __name__ == '__main__':
  main()