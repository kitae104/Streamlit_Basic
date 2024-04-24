# 기본 패키지 
import streamlit as st

# 위젯
# Buttons
name = "홍길동"
if st.button("Submit"):
  st.write(f"Upper : {name.upper()}")

if st.button("Submit", key="new02"):
  st.write(f"Lower : {name.lower()}")

# Radio
status = st.radio("What is your status?", ("Active", "Inactive"))
if status == "Active":
  st.success("You are Active!")
elif status == "Inactive":
  st.warning("Inactive")

# Checkbox
if st.checkbox("Show/Hide"):
  st.text("Showing something")

# Expander
with st.expander("Python"):
  st.text("Python is Awesome!")
  st.image("https://static.streamlit.io/examples/dice.jpg")