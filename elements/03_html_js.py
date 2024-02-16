# -*- coding: utf-8 -*-
import streamlit as st
import streamlit.components.v1 as components

def main():
  st.title("HTML JS Streamlit 적용")
  js_code = '''
  <h3>Hi</h3>
  <script>
  function sayHello() {
    alert('Hello!');
  }
  </script>

  <button onclick="sayHello()">Click me</button>
'''
  components.html(js_code)  # 간단한 경우에는 st.markdown(js_code, unsafe_allow_html=True)로 대체 가능

if __name__ == '__main__':
  main()