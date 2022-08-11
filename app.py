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
Heart disease is the [leading cause of death in the United States](https://www.cdc.gov/heartdisease/facts.htm).
This class of disorders encompass a wide range of cardiovascular problems including but not limited to arrhythmia, atherosclerosis, cardiomyopathy,
congenital heart defects, coronary artery disease, and heart infections.
In 2020, heart disease caused [1 in every 5 deaths (697,000 people)](https://doi.org/10.1161/cir.0000000000001052) and cost [$229 billion dollars from 2017-2018](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files.jsp).
Although with lifestyle adjustments and certain medications can help manage heart disease, early detection and prevention remains one of the most potent
ways to further reduce the risk of developing complications later in life. 
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

st.sidebar.title("Contact")
st.sidebar.info(
    """
    #Inspirit AI: <https://www.inspiritai.com>
    #[GitHub](https://github.com/inspiritai-tech) | [LinkedIn](https://www.linkedin.com/company/inspirit-ai/)
    """
)

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
