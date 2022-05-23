import streamlit as st
import networkx as nx
import FRAKE
import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

st.title("Keyword Extraction Demo: FRAKE")
st.write("그래프와 텍스트의 feature들을  활용하는 키워드 추출 알고리즘의 데모입니다.")


kw = FRAKE.KeywordExtractor(lang='en',hu_hiper=0.4,Number_of_keywords=10)

text = st.text_area("입력")

if st.button('키워드 추출'):
  kws = kw.extract_keywords(text)
  st.write(kws)
