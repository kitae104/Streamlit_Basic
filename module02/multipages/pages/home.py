import streamlit as st
from app import my_variable
from pages.eda import my_calc

st.subheader("Home Page")

st.write(my_variable)

st.title("This is from EDA.py Page")