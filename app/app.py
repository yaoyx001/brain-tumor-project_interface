import streamlit as st
import numpy as np
import nibabel as nib
import requests
#create a Streamlit app instance:
st.set_page_config(page_title='MRI Analyzer', page_icon=':brain:', layout='wide')
st.title('MRI Analyzer')

mri_file = st.file_uploader('Upload an MRI image (NIfTI format)', type=['nii'])

output = st.empty()

#Create a function that analyzes the uploaded MRI image using an API and displays the results:
def analyze_mri(mri_file):
    # Send the MRI data to the API
    api_url = 'https://small-bars-grow-35-205-4-11.loca.lt/predict'
    response = requests.post(api_url, data=mri_file)

    # Parse the API response and extract the analysis results
    result = response.json()
    tumor_risk = result['predictions']
    # Display the analysis results
    output.text(tumor_risk)
def hello():
    api_url = 'https://small-bars-grow-35-205-4-11.loca.lt/hello'
    response = requests.get(api_url, data=mri_file)
    result = response.json()
    output.text(result)

#Handle the user input
if mri_file is not None:
    # Load the MRI data from the uploaded file
    

    # Analyze the MRI data and display the results
    analyze_mri(mri_file)
    hello()
    #output.text('The tumor is high risk')
