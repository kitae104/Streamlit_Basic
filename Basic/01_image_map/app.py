import streamlit as st

st.set_page_config(page_title="이미지 모음", page_icon="./images/logo.png")

st.markdown("""
<style>
h1 {
    color: #FF0000;
}  
img {
    max-height: 300px;
}  
.stExpander div {
    display: flex;
    justify-content: center;
    font-size: 20px;
}
[data-testid='datastExpanderToggleIcon'] {
    visibility: hidden;        
}            

</style>
""", unsafe_allow_html=True) 


st.title("Streamlit을 이용한 이미지 모음")
st.markdown("**:red[이미지]** 를 하나씩 추가해서 **:blue[스타의 사진]** 을 정리하세요.")

mbti_emoji_dict = {
    "INTJ": ":sunglasses:",
    "INTP": ":nerd_face:",
    "ENTJ": ":smiling_imp:",
    "ENTP": ":smirk:",
    "INFJ": ":innocent:",
    "INFP": ":relieved:",
    "ENFJ": ":heart_eyes:",
    "ENFP": ":yum:",
    "ISTJ": ":expressionless:",
    "ISFJ": ":confused:",
    "ESTJ": ":unamused:",
    "ESFJ": ":kissing_heart:",
    "ISTP": ":scream:",
}

init_my_stars = [
    {
        "name": "카리나",
        "mbti": "ENTP",
        "image_url": "https://i.namu.wiki/i/nK3xvRIyMe0KzxUQF_Vn7zJR02Lb9vcPmfhvY_29JufTtB89tRYiK-qp5tV1oj5GoIPEo3ecro-_7n1JKSX4T_hWl1Xb699AmZXa9oP7fSXiR2LGbiVSrXWoSfz0KlAHCoN3ZhaLHnnyAL_FZyuDxw.webp",
    },
    {
        "name": "지젤",
        "mbti": "INFJ",
        "image_url": "https://i.namu.wiki/i/udR9hdHY3Qc8JptfaKQBLG8S_r7mej89xFP1Iz5RfAlrIyg3BG4zPE0LbdfMdyCzdN2awQR2lpUrJ4KnjoCQ3tnzlC6ge0TRibhi8zme5xgjoEXfH0vQPG4pzPZ9clq2jV-ynz1jLm9qyyDiQNr3yw.webp",
    },
    {
        "name": "윈터",
        "mbti": "ENFJ",
        "image_url": "https://i.namu.wiki/i/a7xCMFjEHqPNUCxQvjVMievCViRhyzz0GZxSMJP2T5_tNLYtuQGjhWnpFIDkq1yL_x-ZVNZDKPDdYBflvtc90xxoJujU2I_Vvord-a35SBfXSsDsj8rNeqwMnyGmsz1KGk5Hlq3neJxHA-nkdCjBEg.webp",
    },
    {
        "name": "닝닝",
        "mbti": "INFP",
        "image_url": "https://i.namu.wiki/i/qT-x7_BsscLUVsEuesyFOm_-112dAv3SDlncmuK0zd3dXkVYBuqw7YMhuMQbhEivWRbygat0O0XaCSmZBB2kNPcLKtDqYIOcnB3-CCv2M-ZIUv5clVogc8ueaVi9y8Udi9uWM4JACjWAAa72OfQFyg.webp",
    },
]

example_star = {
    "name": "라이언",
    "mbti": "ENTP",
    "image_url": "https://i.namu.wiki/i/qkyqIPNtVxlT_imBEI2g9EzINfuo44pszLQrhac-KMmMls2m3TQBjQrfT251bKldEsV2_um8vDLUYAWNCUbj1A.webp",
}

# 세션에 추가 : 계속 내용을 유지하기 위해 세션 사용(새로 고침시 초기화) 
if "my_stars" not in st.session_state: 
    st.session_state.my_stars = init_my_stars # 초기값 설정

auto_complete = st.toggle("자동 완성 기능", value=True)
print("")

with st.form(key="my_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input(label="스타 이름", 
                    value=example_star["name"] if auto_complete else "", key="name")
    with col2:
        mbti = st.selectbox(label="MBTI 선택", options=list(mbti_emoji_dict.keys()),                             
                    index=list(mbti_emoji_dict.keys()).index(example_star["mbti"]) if auto_complete else 0, key="mbti")
    image_url = st.text_input(label="이미지 URL", 
                    value=example_star["image_url"] if auto_complete else "", key="image_url")
    submitted = st.form_submit_button(label="등록")

    # 제출 버튼을 누르면 my_stars에 추가
    if submitted:

        if not name:
            st.error("스타 이름을 입력해주세요.")
        else:
            st.success(f"{name}님을 추가했습니다.")

            # 세션에 추가 : 계속 내용을 유지하기 위해 세션 사용 
            st.session_state.my_stars.append(
                {
                    "name": name,
                    "mbti": mbti,
                    "image_url": image_url if image_url else "./images/lion.png",
                }
            )



for i in range(0, len(st.session_state.my_stars), 3):  # 3개씩 묶어서 출력
    row_my_stars = st.session_state.my_stars[i : i + 3]  # 3개씩 묶어서 출력
    cols = st.columns(3)  # 3개의 컬럼 생성
    for j in range(len(row_my_stars)):
        with cols[j]:
            my_star = row_my_stars[j]
            with st.expander(
                label=f'**{i + j + 1}, {my_star["name"]}**', expanded=True
            ):
                st.image(my_star["image_url"], use_column_width=True)
                emoji_types = f'{mbti_emoji_dict[my_star["mbti"]]} {my_star["mbti"]}'
                st.subheader("".join(emoji_types))
                delete_button = st.button("삭제", key=f'{i + j}.', use_container_width=True)
                if delete_button:
                    del st.session_state.my_stars[i + j]
                    st.rerun()
