# -*- coding:utf-8 -*-
import pandas as pd
from utils import load_data
import streamlit as st
from millify import prettify  # 숫자를 사람이 읽기 쉬운 형태로 변환(천단위 쉼표, k, M, B 등)

def run_home():
  total_df = load_data()
  st.markdown("## 대시보드 개요 \n" 
             "이 대시보드는 서울시 부동산 데이터를 활용하여 부동산 시장의 트렌드를 분석하고 시각화한 대시보드입니다. \n"
              "아래는 데이터의 개요입니다.")
  total_df['DEAL_YMD'] = pd.to_datetime(total_df['DEAL_YMD'], format='%Y-%m-%d')      
  total_df['month'] = total_df['DEAL_YMD'].dt.month
  total_df = total_df.loc[total_df['HOUSE_TYPE'] == '아파트', :]

  sgg_nm = st.sidebar.selectbox('자치구 선택', (total_df['SGG_NM'].unique()))
  selected_month = st.sidebar.radio("확인하고 싶은 월을 선택하세요", ['12월', '1월'])
  month_dict = {'12월': 12, '1월': 1}
  st.markdown("<hr>", unsafe_allow_html=True)
  st.subheader(f'{sgg_nm} 자치구 {selected_month} 아파트 가격 개요')
  st.markdown("자치구와 월을 클릭하면 각 지역구의 거래된 **최소가격**, **최대가격**을 확인할 수 있습니다.")
  col1, col2 = st.columns(2)
  filtered_month = total_df[total_df['month'] == month_dict[selected_month]]
  filtered_month = filtered_month[filtered_month['SGG_NM'] == sgg_nm]
  march_min_price = filtered_month['OBJ_AMT'].min()
  march_max_price = filtered_month['OBJ_AMT'].max()

  with col1:
    st.metric(label=f"{sgg_nm} 최소가격(만원)", value=f'{prettify(march_min_price)}')

  with col2:
    st.metric(label=f"{sgg_nm} 최대가격(만원)", value=f'{prettify(march_max_price)}')

  st.markdown("<hr>", unsafe_allow_html=True)
  
  st.markdown("### 아파트 가격 상위 3")
  sorted_df = filtered_month[['SGG_NM', 'BJDONG_NM', 'BLDG_NM', 'BLDG_AREA', 'OBJ_AMT']]
  st.dataframe(sorted_df.sort_values(by='OBJ_AMT', ascending=False).head(3).reset_index(drop=True)) # 가격이 높은 순으로 정렬
  
  st.markdown("<hr>", unsafe_allow_html=True)
  
  st.markdown("### 아파트 가격 하위 3")
  sorted_df = filtered_month[['SGG_NM', 'BJDONG_NM', 'BLDG_NM', 'BLDG_AREA', 'OBJ_AMT']]
  st.dataframe(sorted_df.sort_values(by='OBJ_AMT', ascending=True).head(3).reset_index(drop=True))  # 가격이 낮은 순으로 정렬
  
  st.markdown("<hr>", unsafe_allow_html=True)
  st.caption("출처 : [서울시 부동산 실거래가](https://data.seoul.go.kr/dataList/OA-21275/S/1/datasetView.do)")



  