import streamlit as st

def main():
  st.title("Streamlit Study!")
  st.text("Hello World Text")       # 텍스트 출력
  st.text("한글 사용 여부 확인")    # 한글 사용 가능
  name = "홍길동" 
  st.text(f"안녕하세요. {name}님")   # f-string 사용 가능 

  st.header("Header")
  st.subheader("Subheader")
  st.title("Title")
  st.markdown("## Markdown")
  st.markdown("#### Markdown")

if __name__ == "__main__":
  main()