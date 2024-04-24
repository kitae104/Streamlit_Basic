# 기본 패키지 
import streamlit as st

# 위젯
# Select / Multiple select / Slider
my_lang = ["Python", "Java", "C++", "Go", "C#"]
choice = st.selectbox("당신이 좋아하는 언어를 선택하세요", my_lang)
st.write(f"당신의 선택은 {choice} 입니다.")

# Multiple select
spoken_lang = ("English", "Korean", "Japanese", "Chinese")
choice = st.multiselect("당신이 구사할 수 있는 언어는? ", spoken_lang, default="Korean")
st.write(f"당신의 선택은  {choice} 입니다.")

# Slider
age = st.slider("나이", 1, 100)
st.write(f"당신의 나이는 {age} 입니다.")

# Select Slider
level = st.select_slider("레벨", options=["초급", "중급", "고급"])
st.write(f"당신은 {level} 레벨 입니다.")