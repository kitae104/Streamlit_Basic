import cv2
import streamlit as st
from pathlib import Path
import sys
from ultralytics import YOLO
from PIL import Image

FILE = Path(__file__).resolve() # 현재 파일 경로

ROOT = FILE.parent  # 현재 파일의 부모 경로

if ROOT not in sys.path:
    sys.path.append(str(ROOT)) # 부모 경로를 sys.path에 추가

ROOT = ROOT.relative_to(Path.cwd()) # 상대 경로로 변경

IMAGE = 'Image'
VIDEO = 'Video'

SOURCES_LIST = [IMAGE, VIDEO]

#Image 
IMAGES_DIR = ROOT/'images'
DEFAULT_IMAGE = IMAGES_DIR/'image1.jpg'
DEFAULT_DETECT_IMAGE = IMAGES_DIR/'detectedimage1.jpg'


#Videos 
VIDEO_DIR = ROOT/'videos'
VIDEOS_DICT = {
    'video 1': VIDEO_DIR/'video1.mp4',
    'video 2': VIDEO_DIR/'video2.mp4'
}

#Model 
MODEL_DIR = ROOT/'models'
DETECTION_MODEL = MODEL_DIR/'yolo11n.pt'
SEGMENTATION_MODEL  = MODEL_DIR/'yolo11n-seg.pt'
POSE_ESTIMATION_MODEL = MODEL_DIR/'yolo11n-pose.pt'


# 페이지 설정 
st.set_page_config(
    page_title="YOLOv11",
    page_icon="🤖",
    # layout="wide",
    # initial_sidebar_state="expanded",
)

st.title("객체 탐지 using YOLO11")

st.sidebar.header("Model Configurations")

# 모델 타입 
model_type = st.sidebar.radio("Task", ["Detection", "Segmentation", "Pose Estimation"])

# 신뢰도 설정 
confidence_value = float(st.sidebar.slider("Select Model Confidence Value", 25, 100, 40))/100

# 모델 선택 
if model_type == 'Detection':
    model_path = Path(DETECTION_MODEL)
elif model_type == 'Segmentation':
    model_path = Path(SEGMENTATION_MODEL)
elif model_type ==  'Pose Estimation':
    model_path = Path(POSE_ESTIMATION_MODEL)

# 모델 로드
try:
    model = YOLO(model_path)
except Exception as e:
    st.error(f"모델을 로드할 수 없습니다. 모델 경로를 확인하세요 : {model_path}")
    st.error(e)

st.sidebar.header("Image/Video Config")
source_radio = st.sidebar.radio(
    "Select Source", SOURCES_LIST
)

source_image = None
if source_radio == IMAGE:
    source_image = st.sidebar.file_uploader(
        "Choose an Image....", type = ("jpg", "png", "jpeg", "bmp", "webp")
    )
    col1, col2 = st.columns(2)
    with col1:
        try:
            if source_image is None:
                default_image_path = str(DEFAULT_IMAGE)
                default_image = Image.open(default_image_path)
                st.image(default_image_path, caption = "Default Image", use_column_width=True)
            else:
                uploaded_image  =Image.open(source_image)
                st.image(source_image, caption = "Uploaded Image", use_column_width = True)
        except Exception as e:
            st.error("Error Occured While Opening the Image")
            st.error(e)
    with col2:
        try:
            if source_image is None:
                default_detected_image_path = str(DEFAULT_DETECT_IMAGE)
                default_detected_image = Image.open(default_detected_image_path)
                st.image(default_detected_image_path, caption = "Detected Image", use_column_width = True)
            else:
                if st.sidebar.button("Detect Objects"):
                    result = model.predict(uploaded_image, conf = confidence_value) # YOLO11을 이용한 예측                    
                    boxes = result[0].boxes # 탐지된 객체의 박스 정보
                    result_plotted = result[0].plot()[:,:,::-1] # 탐지된 객체를 표시
                    st.image(result_plotted, caption = "Detected Image", use_column_width = True) 

                    try:
                        with st.expander("Detection Results"):
                            for box in boxes:
                                st.write(box.data) # 탐지된 객체의 정보 출력
                    except Exception as e:
                        st.error(e)
        except Exception as e:
            st.error("Error Occured While Opening the Image")
            st.error(e)

elif source_radio == VIDEO:
    source_video = st.sidebar.selectbox(
        "Choose a Video...", VIDEOS_DICT.keys()
    )
    with open(VIDEOS_DICT.get(source_video), 'rb') as video_file:
        video_bytes = video_file.read()
        if video_bytes:
            st.video(video_bytes)
        if st.sidebar.button("Detect Video Objects"):
            try:
                video_cap = cv2.VideoCapture(
                    str(VIDEOS_DICT.get(source_video))
                )
                st_frame = st.empty()
                while (video_cap.isOpened()):
                    success, image = video_cap.read()
                    if success:
                        image = cv2.resize(image, (720, int(720 * (9/16))))
                        
                        # YOLO11을 이용한 예측
                        result = model.predict(image, conf = confidence_value)
                        
                        # 탐지된 객체를 표시
                        result_plotted = result[0].plot()
                        st_frame.image(result_plotted, caption = "Detected Video",
                                    channels = "BGR",
                                    use_column_width=True)
                    else:
                        video_cap.release()
                        break
            except Exception as e:
                st.sidebar.error("Error Loading Video"+str(e))