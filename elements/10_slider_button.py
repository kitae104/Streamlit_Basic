# -*- coding: utf-8 -*-
# 슬라이더와 버튼 사용하기
import streamlit as st

# 계산이 복잡할 경우 함수로 처리 
def calculate_sales(price, sales_cnt):
  total = price * sales_cnt
  return total

def main():
  st.title("버튼과 슬라이더 다루기")  
  # price = st.slider("가격을 선택하세요", 1000, 10000, value=5000, step=1000)
  price = st.slider("단가 : ", 1000, 10000, value=5000)
  sales_cnt = st.slider("전체 판매 갯수 :", 1, 1000, value=500)
  
  if st.button("매출액 계산"):  # 버튼을 누룰 때만 계산되게 하기 위해 사용 
    result = calculate_sales(price, sales_cnt) 
    st.write(f"전체 판매 가격은 {result:,}원 입니다.")

if __name__ == '__main__':
  main() 

