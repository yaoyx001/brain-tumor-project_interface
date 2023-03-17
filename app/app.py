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

    api_url = 'http://127.0.0.1:8124/predict'
    files = {"file": mri_file.getbuffer()}
    response = requests.post(api_url, files=files)#data=mri_file)

    # Parse the API response and extract the analysis results
    #breakpoint()
    result = response.json()
    tumor_risk = result['predictions']
    #tumor_risk = 'the tumor is a high-grade glioma'
    # Display the analysis results
    output.text(tumor_risk.capitalize() + '!')

#Handle the user input
if mri_file:
    # Load the MRI data from the uploaded file
    

    # Analyze the MRI data and display the results
    analyze_mri(mri_file)
 
    #output.text('The tumor is high risk')
