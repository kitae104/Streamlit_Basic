import pandas as pd
import requests
from io import StringIO
import streamlit as st

def load_original_data():
    # github url 중 raw url을 복사해옵니다.
    url = 'https://raw.githubusercontent.com/kitae104/Streamlit_Basic/main/data/profile.csv'
    response = requests.get(url)
    if response.status_code == 200:
        return pd.read_csv(StringIO(response.text))
    else:
        st.error("Failed to load data from GitHub.")
        return None
    
df = load_original_data()
st.dataframe(df.head())