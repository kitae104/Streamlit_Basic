import streamlit as st 

# TextRank Algorithm
from gensim.summarize import summarize
from sumy.parsers.plaintext import PlaintextParser    # Luhn and LexRank Algorithms
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

import pandas as pd 

import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg') 
import seaborn as sns

def main():
  ''' A Simple NLP App with Streamlit '''
  st.title("Summarizer App")
  menu = ["Home", "About"]
  choice = st.sidebar.selectbox("Menu", menu)
  
  if choice == "Home":
    st.subheader("Summarization")
    raw_text = st.text_area("Enter Text Here")
    
    if st.button("Summarize"):
      with st.expander("Original Text"):
        st.write(raw_text)
      
  else:
    st.subheader("About")

if __name__ == '__main__':
  main()