import streamlit as st
import random
import datetime

st.title(":sparkles:로또 생성기:sparkles:")


def generate_lotto():
    lotto = set()  # 중복을 허용하지 않는 set 자료형

    while len(lotto) < 6:  # 6개의 번호가 모두 모을 때까지 반복
        number = random.randint(1, 46)  # 1부터 45 사이의 난수 생성
        lotto.add(number)  # 생성된 난수를 set에 추가

    lotto = list(lotto) # set 자료형을 list 자료형으로 변환
    lotto.sort() # 번호를 오름차순으로 정렬
    return lotto # 6개의 번호가 담긴 list 반환


st.subheader(f"행운의 번호: :green[{generate_lotto()}]")
st.write(f"생성된 시각: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")

button = st.button("로또를 생성해 주세요!")

if button:
    for i in range(1, 6):
        st.subheader(f"{i}. 행운의 번호: :green[{generate_lotto()}]")
    st.write(f"생성된 시각: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
