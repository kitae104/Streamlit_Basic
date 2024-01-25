import streamlit as st

my_variable = "From Main App.py Page"


def main():
  st.title("Streamlit Multi-page App")
  st.subheader("Main Page")
  st.write(my_variable)

  choice = st.sidebar.selectbox("Sub Menu", ["Pandas", "TensorFlow"])
  if choice == "Pandas":
    st.subheader("Pandas")
    st.write(my_variable)

if __name__ == '__main__':
  main()