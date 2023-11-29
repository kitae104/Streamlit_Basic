import streamlit as st

# 채팅 내용을 기록하는 스토리지 생성
if "messages" not in st.session_state:
  st.session_state.messages = []

# 이전 차트 내용 출력
for message in st.session_state.messages:   # 스토리지에 저장된 메시지를 하나씩 꺼내서
  with st.chat_message(message["role"]):    # 메시지의 role에 따라
    st.write(message["content"])            # 메시지의 내용을 출력


prompt = st.chat_input("무엇이든 질문하세요.")    # 화면의 하단에 입력창이 생김
if prompt:    # 입력창에 입력한 내용이 있으면

  # 입력창에 입력한 내용을 스토리지에 저장
  st.session_state.messages.append({"role":"user", "content":prompt})

  # 입력창에 입력한 내용을 출력
  with st.chat_message("user"):
    st.write(prompt)

  #with st.chat_message("assistant"):
  #  st.write(prompt)

  # custom
  #with st.chat_message("bot", avatar="🤖"):
  #  st.write(prompt)
