import streamlit as st

# 새로운 타이틀 적용
st.title('새로운 웹 애플리케이션 타이틀')

# 특수 이모티콘 삽입 예시 (이모티콘도 변경)
st.title('행복한 개발자 :computer:')

# Header 적용 (새로운 내용)
st.header('여기는 헤더 영역입니다! :rocket:')

# Subheader 적용 (내용 변경)
st.subheader('이것은 새로운 Subheader 입니다')

# 캡션 적용 (새로운 설명 추가)
st.caption('여기는 캡션입니다. 웹 애플리케이션의 설명을 여기에 적어 보세요.')

# 코드 표시 (코드 내용 변경)
new_sample_code = '''
def new_function():
    return '새로운 기능을 추가합니다'
'''
st.code(new_sample_code, language="python")

# 일반 텍스트 (내용 변경)
st.text('여기는 새로운 일반 텍스트입니다. 새로운 설명을 여기에 추가하세요.')

# 마크다운 문법 지원 (내용 변경)
st.markdown('이것은 **새로운 마크다운 문법**입니다.')
st.markdown("텍스트의 색상을 :blue[파란색]으로, 그리고 **:red[빨간색]** 볼트체로 설정할 수 있습니다.")


# LaTex 수식 지원 (피타고라스 정리)
st.latex(r'\sqrt{a^2 + b^2} = c')


