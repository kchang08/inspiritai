import streamlit as st
import time
import numpy as np
import matplotlib.pyplot as plt
from joblib import load
import cv2

st.set_page_config(layout='wide')

st.sidebar.title("Contact")
st.sidebar.info(
    """
    Inspirit AI: <https://www.inspiritai.com>
    [GitHub](https://github.com/inspiritai-tech) | [LinkedIn](https://www.linkedin.com/company/inspirit-ai/)
    """
)

# Intro to Distracted Drivers
st.title("Streamlit Demo: Distracted Drivers")
st.header("This app ...")
st.markdown("Talk about what is classified...")

# Setup
model = load("distracted_driver_cnn.pkl")
ACTIONS = ['Drinking Coffee', 'Using Mirror', 'Using Radio', 'Attentive Driver']

# Interactive photo upload
#f = st.file_uploader("Upload Image")
#if f is not None:
#  file_bytes = np.asarray(bytearray(f.read()), dtype=np.uint8)
#  image = cv2.imdecode(file_bytes, 1)
#  st.image(image, channels="BGR")
#  scores = model.predict(image)
#  st.write(f"The prediction is: {ACTIONS[scores.argmax()]}")
