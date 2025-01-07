# -*- coding: utf-8 -*-
# 사이킷런 기본 예제 
import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import plotly.graph_objects as go

# 데이터 로드 함수 
@st.cache_data    # 캐시 사용
def load_data():
  df = sns.load_dataset("tips")
  return df

@st.cache_resource   # 캐시 사용
def run_model(data, max_depth, min_samples_leaf):
  #특성과 타겟 분리 
  X = data[['total_bill', 'size']]
  y = data['tip']
  
  # 훈련/테스트 데이터 분리
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
  st.write('선택된 max_depth:', max_depth, '& min_samples_leaf:', min_samples_leaf)
  
  random_search = {'max_depth': [i for i in range(max_depth[0], max_depth[1])], 'min_samples_leaf': [min_samples_leaf]}
  
  clf = RandomForestRegressor()
  model = RandomizedSearchCV(estimator=clf, param_distributions=random_search, n_iter=10, cv=4, verbose=1, n_jobs=-1, random_state=42)
  return model.fit(X_train, y_train), X_test, y_test

def predication(model, X_test, y_test):
  # 예측 
  y_test_pred = model.predict(X_test)
  # 성능 평가 
  test_mae = mean_absolute_error(y_test, y_test_pred)
  r2 = r2_score(y_test, y_test_pred)
  
  return y_test_pred, test_mae, r2

def prediction_plot(X_test, y_test, y_test_pred, test_mae, r2):
  # 그래프 그리기 
  fig = go.Figure()
  fig.add_trace(go.Scatter(x=X_test['total_bill'], y=y_test, mode='markers', name='test', marker=dict(color='red')))
  fig.add_trace(go.Scatter(x=X_test['total_bill'], y=y_test_pred, mode='markers', name='prediction', marker=dict(color='blue')))
  fig.update_layout(title='Tip Prediction with RandomForestRegressor', xaxis_title='Total_bill', yaxis_title='Test')  
  
  st.plotly_chart(fig)
  
def main():
  st.title('RandomForestRegressor 예제')
  st.subheader('데이터셋: tips')
  
  df = load_data()
  st.dataframe(df, use_container_width=True)  # 데이터셋 출력, use_container_width=True: 전체 화면 너비에 맞춤
  
  
  max_depth = st.select_slider('Select Max Depth', options=[i for i in range(2, 30)], value=(5, 10))
  min_samples_leaf = st.slider('Minimum samples leaf', min_value=2, max_value=20) #, value=2, step=2)
  
  model, X_test, y_test = run_model(df, max_depth, min_samples_leaf)
  y_test_pred, test_mae, r2 = predication(model, X_test, y_test)
  prediction_plot(X_test, y_test, y_test_pred, test_mae, r2)
  
  st.write('Mean Absolute Error:', test_mae)
  st.write('R2 Score:', r2)
  
if __name__ == '__main__':
  main()