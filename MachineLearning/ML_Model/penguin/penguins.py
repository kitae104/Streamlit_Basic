import pickle

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

st.title("Penguin Classifier")

st.write(
    """6개의 특징을 입력하면 Palmer's Penguins 데이터 세트를 기반으로 구축된 
    모델을 사용하여 펭귄의 종을 예측하는 머신러닝 앱입니다.
    시작하려면 아래 양식을 사용하세요!
    """
)

rfc = None
unique_penguin_mapping = None
penguin_df = None

try:
    penguin_file = st.file_uploader("당신이 가지고 있는 .pkl 파일을 업로드 해주세요.", type="pkl", key="file1")
    if penguin_file is not None:
        rfc = pickle.load(penguin_file)
        penguin_file.close()

    map_file = st.file_uploader("당신이 가지고 있는 .pkl 파일을 업로드 해주세요.", type="pkl", key="file2")
    if map_file is not None:
        unique_penguin_mapping = pickle.load(map_file)
        map_file.close()

    csv_file = st.file_uploader("당신이 가지고 있는 .csv 파일을 업로드 해주세요.", type="csv", key="file3")
    if csv_file is not None:
        penguin_df = pd.read_csv(csv_file)
        csv_file.close()
except Exception as e:
    # 오류 메시지 출력
    print(f"An error occurred while uploading the file: {e}")



with st.form("user_inputs"):
    island = st.selectbox("Penguin Island", options=["Biscoe", "Dream", "Torgerson"])
    sex = st.selectbox("Sex", options=["Female", "Male"])
    bill_length = st.number_input("Bill Length (mm)", min_value=0)
    bill_depth = st.number_input("Bill Depth (mm)", min_value=0)
    flipper_length = st.number_input("Flipper Length (mm)", min_value=0)
    body_mass = st.number_input("Body Mass (g)", min_value=0)
    st.form_submit_button()

island_biscoe, island_dream, island_torgerson = 0, 0, 0
if island == "Biscoe":
    island_biscoe = 1
elif island == "Dream":
    island_dream = 1
elif island == "Torgerson":
    island_torgerson = 1

sex_female, sex_male = 0, 0
if sex == "Female":
    sex_female = 1
elif sex == "Male":
    sex_male = 1

new_prediction = rfc.predict(
    [
        [
            bill_length,
            bill_depth,
            flipper_length,
            body_mass,
            island_biscoe,
            island_dream,
            island_torgerson,
            sex_female,
            sex_male,
        ]
    ]
)

st.subheader("Predicting Your Penguin's Species:")
prediction_species = unique_penguin_mapping[new_prediction][0]
st.write(f"We predict your penguin is of the {prediction_species} species")
# st.write(
#     """We used a machine learning
#     (Random Forest) model to predict the
#     species, the features used in this
#     prediction are ranked by relative
#     importance below."""
# )
st.image("feature_importance.png")

st.write(
    """Below are the histograms for each
continuous variable separated by penguin species.
The vertical line represents the inputted value."""
)

fig, ax = plt.subplots()
ax = sns.displot(x=penguin_df["bill_length_mm"], hue=penguin_df["species"])
plt.axvline(bill_length)
plt.title("Bill Length by Species")
st.pyplot(ax)

fig, ax = plt.subplots()
ax = sns.displot(x=penguin_df["bill_depth_mm"], hue=penguin_df["species"])
plt.axvline(bill_depth)
plt.title("Bill Depth by Species")
st.pyplot(ax)

fig, ax = plt.subplots()
ax = sns.displot(x=penguin_df["flipper_length_mm"], hue=penguin_df["species"])
plt.axvline(flipper_length)
plt.title("Flipper Length by Species")
st.pyplot(ax)