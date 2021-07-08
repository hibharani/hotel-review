# -*- coding: utf-8 -*-
"""
@author: Basavaraj.Korwar
"""

# -*- coding: utf-8 -*-
"""
@author: Basavaraj.Korwar
"""


import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(txtDescription):   
    prediction=classifier.predict([txtDescription])
    print(prediction)
    return prediction



def main():
    """st.title("Capstone Project")"""
    html_temp = """
    <div style="background-color:grey;padding:5px">
    <h2 style="color:white;text-align:center;">GL - Semi Ruled Chat Bot</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    txtCpuntry = st.text_input("Country","")
    txtState = st.text_input("State","")
    txtGender = st.text_input("Gender","")
    txtEmployeeType = st.text_input("Emplotee Type","")
    txtDescription = st.text_input("Description","")    
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(txtDescription)
    st.success('The Final output is {}'.format(result))    

if __name__=='__main__':
    main()
    
    
    
