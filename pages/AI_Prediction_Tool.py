import streamlit as st
from joblib import load

st.set_page_config(layout='wide')

# Demo
st.header("🫀 Try: AI Risk Assessment Tool 🩺")
st.markdown(
  """
  Enter in your values for **systolic blood pressure** and **maximum heart rate** and let the AI predict whether
  you are at risk for heart disease.
  Note: This tool is meant for informational purposes only. Always consult with a medical professional
  regarding your unique situation. Cardiac risk assessments are not helpful for those who have already
  had a cardiac event (e.g. heart attack, stroke, or heart failure).
  """
)

# Load DecisionTree Model
model = load("heart-disease-model.joblib")

# Collect User Data
bp = st.number_input("Enter Your Systolic Blood Pressure", min_value=100, max_value = 180, value=120, step=1)
hr = st.number_input("Enter Your Maximum Heart Rate (during excercise, in beats per minute)", min_value=80, max_value = 230, value=165, step=1)
input = [[bp, hr]]

submit = st.button("Submit Response")

def make_prediction(model, input):
  return model.predict(input)

def get_app_response(prediction):
  if prediction == 1:
    st.subheader("You may be at risk for heart disease.")
    st.write("Here are some [resources](https://www.mayoclinic.org/diseases-conditions/heart-disease/symptoms-causes/syc-20353118) to check out to decide on the next best step.")
  elif prediction == 0:
    st.subheader("According to our machine learning model, you are not likely to be at risk for heart disease.")
    st.write("Here is a [resource](https://health.gov/myhealthfinder/health-conditions/heart-health/keep-your-heart-healthy) on how to maintain your heart health.")
  else:
    st.error("Oops, we've run into an error! Try refreshing the page.")

if submit:
  prediction = make_prediction(model, input)
  get_app_response(prediction)
else:
  st.subheader("Click the Submit Button to Generate Your AI Prediction")
