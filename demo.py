import streamlit as st
import networkx as nx
import FRAKE
import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

st.title("Keyword Extraction Demo: FRAKE")
st.write("This is a keyword extraction demo using FRAKE combined with Graph Features.")


kw = FRAKE.KeywordExtractor(lang='en',hu_hiper=0.4,Number_of_keywords=10)

text = st.text_input("입력")

if st.button('출력(키워드 리스트)'):
  kws = kw.extract_keywords(text)
  st.write(kws)
