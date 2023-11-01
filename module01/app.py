# 기본 패키지 
import streamlit as st

# 위젯
# Select / Multiple select / Slider
my_lang = ["Python", "Java", "C++", "Go", "C#"]
choice = st.selectbox("Choose Language", my_lang)
st.write(f"You selected {choice}")

# Multiple select
spoken_lang = ("English", "Korean", "Japanese", "Chinese")
choice = st.multiselect("Spoken Language", spoken_lang, default="Korean")
st.write(f"You selected {choice}")

# Slider
age = st.slider("Age", 1, 100)
st.write(f"Your age is {age}")

# Select Slider
level = st.select_slider("Level", options=["Beginner", "Intermediate", "Advanced"])
st.write(f"Your level is {level}")