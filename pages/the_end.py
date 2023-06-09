import streamlit as st
from PIL import Image

st.divider()
st.title(':blue[Thank you for your attention !] :green_heart:')
st.divider()
image = Image.open('pict/man.jpg')

st.image(image)

st.balloons()