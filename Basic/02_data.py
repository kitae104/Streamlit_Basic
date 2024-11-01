import streamlit as st
import pandas as pd
import numpy as np

# 새로운 타이틀 적용
st.title('데이터 분석 애플리케이션')

# DataFrame 생성 (내용 변경)
df = pd.DataFrame({
    'Product': ['A', 'B', 'C', 'D'],
    'Sales': [100, 150, 200, 250],
})

# DataFrame 출력
# use_container_width=True로 설정하여 데이터프레임이 전체 화면 너비를 차지하도록 변경
st.dataframe(df, use_container_width=False)

# 테이블(static) 출력 (내용 유지)
# DataFrame과는 다르게 interactive 한 UI 를 제공하지 않습니다.
st.table(dataframe)

# 메트릭 - 상태를 표현할 때 사용 (내용 변경)
st.metric(label="습도", value="65%", delta="-5% 감소")
st.metric(label="애플 주가", value="$150", delta="$5 증가")

# 컬럼으로 영역을 나누어 표기한 경우 (데이터 및 단위 변경)
col1, col2, col3 = st.columns(3)
col1.metric(label="비트코인 BTC", value="$40,000", delta="2.5% 상승")
col2.metric(label="이더리움 ETH", value="$2,800", delta="3.1% 상승")
col3.metric(label="리플 XRP", value="$0.85", delta="-0.5% 하락")
