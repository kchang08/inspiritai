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

with st.expander("Why is Detecting Distracted Driving Challenging?"):
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
    AI would serve two main purposes: to provide output to the driver (via alerts) 
    and to specify a vehicle reaction in the form of a brake, steer change, etc. 
    Using AI and visual AI (e.g. cameras and sensors), it is possible to process
    the driver's actions in real-time so that dangerous circumstances can be
    reduced. 
    """
  )
