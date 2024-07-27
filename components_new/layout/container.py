import streamlit as st
import numpy as np

with st.container():
    st.write("This is inside the container")
 
    st.bar_chart(np.random.randn(50, 3))

st.write("This is outside the container")

with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)
st.write("Outside the form")