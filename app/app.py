import streamlit as st
import numpy as np
import nibabel as nib
import requests
import time
#create a Streamlit app instance:
st.set_page_config(page_title='Brain Tumor Analyzer', page_icon=':brain:', layout='wide')
st.title('Brain Tumor Analyzer')

mri_file = st.file_uploader('Upload an MRI T1 image (NIfTI format)', type=['nii'])

output = st.empty()

#Create a function that analyzes the uploaded MRI image using an API and displays the results:
def analyze_mri(mri_file):
    # Send the MRI data to the API

    api_url = 'https://tangy-clocks-yawn-35-205-4-11.loca.lt/predict'
    files = {"file": mri_file.getbuffer()}
    response = requests.post(api_url, files=files)#data=mri_file)

    # Parse the API response and extract the analysis results
    #breakpoint()
    result = response.json()
    tumor_risk = result['predictions']
    #tumor_risk = 'the tumor is a high-grade glioma'
    # Display the analysis results
    #output.text(tumor_risk)
    return tumor_risk

#Handle the user input

if mri_file:
    # Load the MRI data from the uploaded file
    with st.spinner('Analyzing...'):
        prediction = analyze_mri(mri_file)
    st.success('Prediction is done', icon="ℹ️")
    st.subheader(prediction)
