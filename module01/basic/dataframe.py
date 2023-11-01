import streamlit as st
import pandas as pd

# Display Json
st.json({'name':'홍길동', 'age':20})

mycode = '''
def hello():
  print("Hello, Streamlit!")
'''

st.code(mycode, language='python')

df = pd.read_csv('iris.csv')

# st.dataframe(df, 200, 100)

st.dataframe(df.style.highlight_max(axis=0))

st.write(df.head())

# static table 
st.table(df)

