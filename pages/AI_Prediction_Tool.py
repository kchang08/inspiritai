import streamlit as st
from joblib import load
import numpy as np
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
import tensorflow
from tensorflow.keras.models import load_model
from PIL import Image, ImageOps

st.set_page_config(layout='wide')

# Demo
st.header("Try: AI Distracted Driver Classifier")
st.markdown(
  """
  This app labels images of drivers as attentive and non-attentive. 
  The four labels are Drinking Coffee, Using Mirror, Using Radio, and Attentive Driver. 
  """
)

# Load CNN model
model = load_model('keras_model.h5')

# Interactive photo upload
f = st.file_uploader("Upload Image")

if f is not None:
  image=Image.open(f) 
  st.image(image, channels="BGR")
  image = image.convert('RGB')
  #resize the image to a 224x224 with the same strategy as in TM2:
  #resizing the image to be at least 224x224 and then cropping from the center
  size = (224, 224)
  image = ImageOps.fit(image, size, Image.ANTIALIAS)
  #turn the image into a numpy array
  image_array = np.asarray(image)
  # Normalize the image
  normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
  # run the inference
  prediction = model.predict(np.array([normalized_image_array]))
  
  pred = np.argmax(prediction)
  
  if pred == 3:
    st.subheader("The driver appears to be drinking coffee and is a distracted driver.")
  elif pred == 1:
    st.subheader("The driver appears to be using a mirror and is a distracted driver.")
  elif pred == 0:
    st.subheader("The driver appears to be using the radio and is a distracted driver.")
  elif pred == 2:
    st.subheader("The driver appears to be attentive 😊.")
  else:
    st.error("Oops, we've run into an error! Try refreshing the page.")
