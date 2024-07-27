# -*- coding: utf-8 -*-
# number date input 사용하기 
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import yfinance as yf
  
def main():
  st.sidebar.title("SideBar 다루기")  
  
  # ticker 텍스트 구현 
  ticker = st.sidebar.text_input('Ticker 입력(예 : AAPL)', 'AAPL')
  st.sidebar.markdown('Tickers Link : [All Stock Symbols](https://stockanalysis.com/stocks/)')  # 링크 추가
  
  # 날짜 입력 구현 
  start_date = st.sidebar.date_input('Start Date', value=pd.to_datetime('2023-01-01'))
  end_date = st.sidebar.date_input('End Date', value=pd.to_datetime('today'))
  
  # 데이터 다운로드
  data = yf.download(ticker, start=start_date, end=end_date)
  
  # 시각화 선택 구현 
  chart_type = st.sidebar.radio('Select Chart Type', ('Candlestick', 'Line'))
  candlestick = go.Candlestick(x=data.index, open=data['Open'], high=data['High'], low=data['Low'], close=data['Close'])
  line = go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Close')
  
  if chart_type == 'Candlestick':
    fig = go.Figure(data=[candlestick]) # 캔들스틱 차트
  elif chart_type == 'Line':
    fig = go.Figure(data=[line])  # 라인 차트
  else:
    pass
  
  fig.update_layout(title=f'{ticker} Stock {chart_type} Chart', xaxis_title='Date', yaxis_title='Price')
  
  st.plotly_chart(fig)
  st.markdown("<hr>", unsafe_allow_html=True)  # 구분선 추가
  
  # 테이블 출력 
  num_row = st.sidebar.number_input('Number of Rows to Display', min_value=1, max_value=len(data), value=10)
  st.dataframe(data[-num_row:].reset_index().sort_index(ascending=False).set_index('Date'), use_container_width=True)
  
if __name__ == '__main__':
  main() 

