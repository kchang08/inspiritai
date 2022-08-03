import streamlit as st
import time
import numpy as np
import matplotlib.pyplot as plt
from joblib import load
import pickle

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
st.header("This app labbels images of drivers as attentive and non-attentive.")
st.markdown("The four labels are Drinking Coffee, Using Mirror, Using Radio, and Attentive Driver. Example images of each are shown below.")
st.image("coffee.png")
st.caption("Drinking Coffee")
st.image("mirror.png")
st.caption("Using Mirror")
st.image("radio.png")
st.caption("Using Radio")
st.image("attentive.png")
st.caption("Attentive Driver")

# Setup
model = load('distracted_drivers_cnn.pkl')
ACTIONS = ['Drinking Coffee', 'Using Mirror', 'Using Radio', 'Attentive Driver']

# Interactive photo upload
f = st.file_uploader("Upload Image")
"""
if f is not None:
  file_bytes = np.asarray(bytearray(f.read()), dtype=np.uint8)
  image = cv2.imdecode(file_bytes, 1)
  st.image(image, channels="BGR")
  scores = model.predict(image)
  st.write(f"The prediction is: {ACTIONS[scores.argmax()]}")
"""
