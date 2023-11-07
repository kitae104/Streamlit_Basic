# 기본 패키지 
import streamlit as st

# 미디어 파일 (이미지, 동영상, 오디오)
# 이미지
from PIL import Image
img = Image.open("data/image_03.jpg")
st.image(img, width=300, caption="Streamlit 이미지")
st.image("data/image_03.jpg", use_column_width=True, caption="Streamlit 이미지")
st.image("https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FwkZpB%2Fbtr53FYzZ9T%2FZSAM2MSk2B5zJ1yErKRKm0%2Fimg.jpg")

# 동영상
video_file = open("data/secret_of_success.mp4", "rb").read()
st.video(video_file, start_time=0)

# 오디오
audio_file = open("data/song.mp3", "rb").read()
st.audio(audio_file, format="audio/mp3")