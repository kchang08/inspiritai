import streamlit as st
from joblib import load
import numpy as np
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
import tensorflow
from tensorflow.keras.models import load_model
from PIL import Image

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
ACTIONS = ['Drinking Coffee', 'Using Mirror', 'Using Radio', 'Attentive Driver']

# Interactive photo upload
f = st.file_uploader("Upload Image")

if f is not None:
  img=image.load_img(f) 
  st.image(img, channels="BGR")
  x=image.img_to_array(img)
  x=np.expand_dims(x, axis=0)
  images = np.vstack([x])

  classes = model.predict(images)
  prediction = classes.argmax()
  if prediction == 1:
    st.subheader("The driver is likely distracted.") 
    st.write(f"The driver is believed to be: {ACTIONS[prediction]}")
  elif prediction == 2:
    st.subheader("The driver is likely distracted.") 
    st.write(f"The driver is believed to be: {ACTIONS[prediction]}")
  elif prediction == 3:
    st.subheader("The driver is likely distracted.") 
    st.write(f"The driver is believed to be: {ACTIONS[prediction]}")
  elif prediction == 4:
    st.subheader("The driver seems to be attentive!") 
  else:
    st.error("Oops, we've run into an error! Try refreshing the page.")
