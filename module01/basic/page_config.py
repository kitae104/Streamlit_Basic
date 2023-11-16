# 기본 패키지
import streamlit as st
from PIL import Image

# 이미지 불러오기
image = Image.open('data/Logo.png')

# 기본적인 페이지 설정1
#st.set_page_config(page_title='기태홈', page_icon=image, layout='centered', initial_sidebar_state="auto", menu_items=None)

# 기본적인 페이지 설정2
# PAGE_CONFIG = {"page_title": "기태홈", "page_icon": image, "layout": "centered"}
# st.set_page_config(**PAGE_CONFIG)

st.set_page_config(
    page_title="kitae App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)


def main():
    st.title("Hello Streamlit Lovers 😊")


if __name__ == '__main__':
    main()
