import streamlit as st
import pyjokes

st.title('Here is a joke from pyjokes')
st.text(pyjokes.get_joke())
