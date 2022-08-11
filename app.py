import streamlit as st

st.set_page_config(layout='wide')

# Create a sidebar and populate with content
st.sidebar.title("About")
st.sidebar.info(
    """
    Web App URL: <https://inspiritai-tech-demo-distracted-drivers-app-mx4kvv.streamlitapp.com/>
    \n
    GitHub Respository: <https://github.com/inspiritai-tech/demo-distracted-drivers>
    """
)

st.sidebar.title("Contact")
st.sidebar.info(
    """
    Inspirit AI: <https://www.inspiritai.com>
    [GitHub](https://github.com/inspiritai-tech) | [LinkedIn](https://www.linkedin.com/company/inspirit-ai/)
    """
)

# Title
st.title("AI Powered Distracted Driver Classifier")
st.subheader("Determine a Driver's Attention")

# Distracted Driver Image
st.image("distracted_driver.jpeg")
st.caption("Photo Credit: (https://mkl-sitecore102-prod-326360-cdn-endpoint.azureedge.net/~/media/specialty/2018-web/small-business/what-is-distracted-driving.jpg?rev=f43a43df99e44dd3913a2a40db23ea19).")

# Introduction
st.markdown(
'''
At least nine people in the United States die and another 100 are injured each day in crashes caused by distracted driving (https://www.wardsauto.com/industry-voices/nothing-artificial-about-intelligence-reducing-distracted-driving).
And while texting and general cell phone usage is the leading cause, distracted driving also includes using the radio, eating, and applying makeup. The economic impact of distracted driving is \$40M per year - comparable to the \$44M 
per year from DUIs. In 2020, distracted driving claimed the lives of 3,142 people (https://www.nhtsa.gov/risky-driving/distracted-driving). And while there are a considerable number of policies that target the reduction of distracted driving, 
it is believed that at any given moment in the day, there is still over 350,000 distracted drivers in the United States.
'''
)

# Motivation

with st.expander("Why is Detecting Heart Disease Challenging?"):
  st.markdown(
    """
    Typically, patients first learn of their suspected risk from their general practitioners which may involve lengthy
    assessments, tests, and referrals to specialists like cardiologists. Costly tests including electrocardiograms, echocardiograms, blood tests,
    MRI scans, CT scans, X-Rays, and more could be run by a patients' medical team to diagnose specific problems.
    For many, however, access to heathcare poses significant barriers to entry including time, money, insurance, and more.
    """
  )

# Solution
with st.expander("How AI Can Help"):
  st.markdown(
    """
    What if we could give some autonomy and power back to patients with an AI powered tool that screens individuals
    based on simple lab results that any doctor or nurse could perform? Here, you will see one such example solution based on a
    dataset of hundreds of patients with and without heart disease. By training a model to learn the importance of predictors
    (such as age or cholesterol), this algorithm can help guide patients toward seeking additional care or making lifestyle changes
    to further reduce their risk.
    What's more, the larger the dataset becomes, the more accurate this classifer can become, improving predictions across age, ethnicity,
    race, sex, and more.
    """
  )


"""import streamlit as st
import time
import numpy as np
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
from joblib import load
import tensorflow
from tensorflow.keras.models import load_model
from PIL import Image

st.set_page_config(layout='wide')

# Intro to Distracted Drivers
st.title("Streamlit Demo: Distracted Drivers")

st.header("About the App")
st.markdown("This app labels images of drivers as attentive and non-attentive. It uses a CNN model.")
st.markdown("The four labels are Drinking Coffee, Using Mirror, Using Radio, and Attentive Driver. Example images of each are shown below.")
st.image("coffee.png",width=200)
st.caption("Drinking Coffee")
st.image("mirror.png",width=200)
st.caption("Using Mirror")
st.image("radio.png",width=200)
st.caption("Using Radio")
st.image("attentive.png",width=200)
st.caption("Attentive Driver")

# Setup
model = load_model('cnn_model.h5')
ACTIONS = ['Drinking Coffee', 'Using Mirror', 'Using Radio', 'Attentive Driver']

st.header("Try out the App")
st.markdown("Upload an image to test out the model!")

# Interactive photo upload
f = st.file_uploader("Upload Image")

if f is not None:
  #file_bytes = np.asarray(bytearray(f.read()), dtype=np.uint8)
  img=image.load_img(f, target_size=(64, 64)) # edit the target_size
  st.image(img, channels="BGR")
  x=image.img_to_array(img)
  x=np.expand_dims(x, axis=0)
  images = np.vstack([x])

  classes = model.predict(images, batch_size=16)
  st.write(f"The driver in the image has the following prediction: {ACTIONS[classes.argmax()]}")"""
