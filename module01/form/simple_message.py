import streamlit as st

def main():
  st.title("Streamlit Message App")  
  st.subheader("Message App") 

  # Docs
  # st.help(st.form)

  with st.form(key="my_form", clear_on_submit=True): # 폼 출력후 입력값 초기화
    firstname = st.text_input("First Name")
    lastname = st.text_input("Last Name")
    message = st.text_area("Message", height=100) 
    submit_button = st.form_submit_button(label="Submit") 

  if submit_button:
    st.info("Results")
    result = firstname + lastname + "@.gmail.com"
    st.write(result)

if __name__ == '__main__':
  main()