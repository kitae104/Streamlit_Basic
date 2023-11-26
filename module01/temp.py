import streamlit as st

def main():
  st.title("Streamlit Message App")  

  menu = ["Home", "About"]
  choice = st.sidebar.selectbox("Menu", menu)
  if choice == "Home":
    st.subheader("Message App")   


if __name__ == '__main__':
  main()