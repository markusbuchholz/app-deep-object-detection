# Making the necessary imports
import streamlit as st
import cv2
import numpy as np
st.title("First Streamlit Web Application")
st.markdown("This simple web application renders the \
uploaded images into grayscale mode.")

st.sidebar.title("First Streamlit Web Application")
st.sidebar.markdown("This simple web application renders the \
uploaded images into grayscale mode.")

uploaded_file=st.sidebar.file_uploader(label="Upload Image",type=["jpg","jpeg","png"],key="1")
if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()),\
    dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    st.subheader("Grayscale Image")
    st.image(image=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY),width=400)