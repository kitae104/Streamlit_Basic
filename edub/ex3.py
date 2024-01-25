import streamlit as st
import random

# 앱이 처음 실행될 때 한 번만 실행되는 부분
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    

def main():
    st.title("랜덤 수 맞추기 게임")
    st.write("추측 수 : " + str(st.session_state.secret_number))

    guess = st.number_input("1에서 100 사이의 수를 추측하세요:", min_value=1, max_value=100, step=1)

    if st.button("확인"):
        if guess == st.session_state.secret_number:
            st.success("축하합니다! 정답을 맞췄습니다.")
        elif guess < st.session_state.secret_number:
            st.info("너무 작습니다. 더 큰 수를 추측해보세요.")
        else:
            st.info("너무 큽니다. 더 작은 수를 추측해보세요.")

if __name__ == "__main__":
    main()