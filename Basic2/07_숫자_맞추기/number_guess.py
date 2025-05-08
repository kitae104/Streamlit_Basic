import streamlit as st
import random

# 앱 초기화
if "target" not in st.session_state:
    st.session_state.target = random.randint(1, 100)  # 랜덤 숫자 설정
    st.session_state.attempts = 0                    # 시도 횟수 초기화
    st.session_state.guess = None                   # 사용자 입력값 초기화
    st.session_state.message = ""                  # 메시지 초기화

# 앱 제목
st.title("숫자 맞추기 게임 🎮")
st.write("1부터 100 사이의 숫자를 맞춰보세요!")

# 사용자 입력 받기
user_guess = st.number_input("숫자를 입력하세요:", min_value=1, max_value=100, step=1, key="guess_input")

# 버튼 클릭 이벤트
if st.button("제출"):  
    st.session_state.attempts += 1  # 시도 횟수 증가
    st.session_state.guess = user_guess

    # 결과 처리
    if user_guess < st.session_state.target:
        st.session_state.message = "⬆️ UP! 더 큰 숫자를 입력하세요."
    elif user_guess > st.session_state.target:
        st.session_state.message = "⬇️ DOWN! 더 작은 숫자를 입력하세요."
    else:
        st.session_state.message = f"🎉 정답입니다! {st.session_state.attempts}번 만에 맞췄습니다!"
        st.balloons()

# 메시지 출력
if st.session_state.message:
    if st.session_state.guess != st.session_state.target:
        st.error(st.session_state.message)
    else:
        st.success(st.session_state.message)

# 게임 재시작 버튼
if st.session_state.guess == st.session_state.target:
    if st.button("다시 시작"):
        st.session_state.target = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.guess = None
        st.session_state.message = ""


# 디버깅용: 정답 보기 (개발 중에만 활성화)
st.write(f"(정답: {st.session_state.target})")