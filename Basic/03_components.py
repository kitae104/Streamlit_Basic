import streamlit as st
import pandas as pd
from datetime import datetime as dt
import datetime

# 버튼 클릭
button = st.button('이 버튼을 눌러보세요!')

if button:
    st.write(':blue[와우! 버튼]을 눌렀군요! :star_struck:')

# 파일 다운로드 버튼
# 샘플 데이터 생성
dataframe = pd.DataFrame({
    '번호': [1, 2, 3, 4],
    '점수': [95, 88, 76, 92],
})

# 다운로드 버튼 연결
st.download_button(
    label='점수표를 CSV로 다운로드하세요!',
    data=dataframe.to_csv(), 
    file_name='점수표.csv', 
    mime='text/csv'
)

# 체크 박스
agree = st.checkbox('이벤트에 참여하시겠습니까?')

if agree:
    st.write('참여해주셔서 감사해요! 행운을 빌어요 :four_leaf_clover:')

# 라디오 선택 버튼
mbti = st.radio(
    '당신의 MBTI는 무엇인가요?',
    ('ISTJ', 'ENFP', '잘 모르겠어요'))

if mbti == 'ISTJ':
    st.write('당신은 :blue[논리적이고 신중한 사람]이군요! :thinking_face:')
elif mbti == 'ENFP':
    st.write('당신은 :green[창의적이고 활발한 사람]이네요! :partying_face:')
else:
    st.write("MBTI를 알아보는 것도 재미있을 거예요! :mag:")

# 선택 박스
mbti = st.selectbox(
    '당신의 MBTI를 선택해 주세요',
    ('ISTJ', 'ENFP', '잘 모르겠어요'), 
    index=2
)

if mbti == 'ISTJ':
    st.write('당신은 :blue[현실적인 계획자] 이시네요!')
elif mbti == 'ENFP':
    st.write('당신은 :green[열정적인 도전가] 이시네요!')
else:
    st.write("당신에 대해 :red[더 알고 싶어요]!")

# 다중 선택 박스
options = st.multiselect(
    '가장 좋아하는 과일은 무엇인가요?',
    ['딸기', '망고', '오렌지', '사과', '바나나'],
    ['딸기', '망고'])

st.write(f'당신이 고른 과일은: :red[{options}] 입니다! :apple:')

# 슬라이더
values = st.slider(
    '오늘의 기분을 0에서 100으로 표현해 보세요! :sparkles:',
    0.0, 100.0, (30.0, 80.0))
st.write('당신의 기분 범위:', values)

start_time = st.slider(
    "언제 게임 파티를 열고 싶으세요?",
    min_value=dt(2020, 1, 1, 0, 0), 
    max_value=dt(2020, 1, 7, 23, 0),
    value=dt(2020, 1, 3, 18, 0),
    step=datetime.timedelta(hours=1),
    format="MM/DD/YY - HH:mm")
st.write("파티를 열 시간:", start_time)

# 텍스트 입력
title = st.text_input(
    label='방학 때 가고 싶은 장소가 있나요?', 
    placeholder='장소를 입력해 주세요!'
)
st.write(f'당신이 가고 싶은 장소는 :violet[{title}]입니다!')

# 숫자 입력
number = st.number_input(
    label='당신의 나이는 몇 살인가요?', 
    min_value=10, 
    max_value=100, 
    value=15,
    step=1
)
st.write('당신의 나이는: ', number, '살 이군요!')
