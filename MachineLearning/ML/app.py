# -*- coding: utf-8 -*-
# 데이터 셋 처리하기 
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score # 평가 지표(분류)

import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np

@st.cache_data    # 캐시 사용
def load_data():
  df = sns.load_dataset("tips")
  return df

def main():
  st.title("Dataset 전처리")  

  tips = load_data()
  st.dataframe(tips.head(), use_container_width=True)

  # 데이터 가공(성별을 문자에서 숫자로 변경 0 = Female, 1 = Male) 
  y = tips['sex'].apply(lambda x: 1 if x == 'Male' else 0) 
  X = tips.drop('sex', axis=1)

  st.write("* 데이터의 형태 확인 :  ")
  st.write(f"tips.shape = {tips.shape}, X.shpae = {X.shape}, y.shape = {y.shape}")

  # 훈련 데이터 및 테스트 데이터로 분리 8:2
  # 훈련 데이터 및 검증 데이터 분리 6:4
  # 훈련 데이터 -> 학습, 검증 데이터 검증 -> 테스트 데이터
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 

  st.write("* 학습 데이터의 형태 확인 :  ")
  st.write(f"X_train.shape = {X_train.shape}, X_test.shpae = {X_test.shape}, y_train.shape = {y_train.shape}, y_test.shpae = {y_test.shape}")

  st.dataframe(X_train.head(), use_container_width=True)

  # 데이터 전처리 - 원 핫 인코딩 
  categorical_features = ['smoker', 'day', 'time']
  numerical_features = ['total_bill', 'tip', 'size']

  preprocessor = ColumnTransformer(
    transformers=[
      ('num', StandardScaler(), numerical_features),
      ('cat', OneHotEncoder(), categorical_features)
    ])
  
  X_train = preprocessor.fit_transform(X_train)

  st.write("* 전처리 후 학습 데이터의 형태 확인 :  ")
  st.dataframe(pd.DataFrame(X_train).head(), use_container_width=True)

  # 모델 만들기 
  model = DecisionTreeClassifier()

  # 파이프라인 만들기
  pipeline = Pipeline(steps=[('preprocessor', preprocessor), ('classifier', model)])
  # pipeline.fit(X_train, y_train)

if __name__ == '__main__':
  main()