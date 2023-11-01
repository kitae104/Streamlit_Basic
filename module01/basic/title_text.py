import streamlit as st

def main():

  # 텍스트 출력
  st.title("Streamlit Study!")
  st.text("Hello World Text")       # 텍스트 출력
  st.text("한글 사용 여부 확인")    # 한글 사용 가능
  name = "홍길동" 
  st.text(f"안녕하세요. {name}님")   # f-string 사용 가능 

  # 헤더 출력
  st.header("Header")
  st.subheader("Subheader")
  st.title("Title")
  st.markdown("## Markdown")
  st.markdown("#### Markdown")

  # 색상이 있는 텍스트 출력
  st.success("Successful")
  st.warning("Warning")
  st.info("This is information")
  st.error("This is error")
  st.exception("This is exception")
  
  # write() 함수를 이용한 출력
  st.write("Normal Text")
  st.write("## This is a markdown text")
  st.write(1 + 2)
  st.write(dir(st))

  # help 설명
  st.help(range)

  

if __name__ == "__main__":
  main()