import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


def main():
    # 폰트 파일 업로드
    uploaded_file = st.file_uploader("한글 폰트 파일 업로드", type=["ttf"])

    if uploaded_file is not None:
        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # 업로드된 폰트 파일 경로 설정
        font_path = uploaded_file.name   # "NanumGothic.ttf" - 여기에 폰트 파일 연결

        # 폰트 등록
        font_prop = fm.FontProperties(fname=font_path)

        # Matplotlib 설정
        plt.rcParams["font.family"] = font_prop.get_name()

        # 한글이 포함된 그래프 생성
        plt.figure(figsize=(8, 6))
        plt.plot(["서울", "대전", "대구", "부산"], [1, 4, 9, 16])
        plt.title("한글 폰트 적용 Test", fontproperties=font_prop)
        plt.xlabel("x축", fontproperties=font_prop)
        plt.ylabel("y축", fontproperties=font_prop)
        plt.xticks(fontproperties=font_prop)
        st.pyplot(plt)


if __name__ == "__main__":
    main()
