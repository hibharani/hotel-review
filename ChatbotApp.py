import numpy as np
import pickle
import pandas as pd
import streamlit as st 
from collections import OrderedDict
from joblib import load

def processinput():
    answers = []
    for key in st.session_state.keys():
            if(key.startswith('answer')):
                answers.append(st.session_state[key])

    #Convert this into the format needed for the model file!
    input = OrderedDict({
        'Country' : answers[0],
        'Local': answers[1],
        'Industry Sector': answers[4],
        'Potential Accident Level': answers[5],
        'Gender': answers[2],
        'Employee Type': answers[3],
        'Critical Risk': answers[6],
        'Description': answers[7],
        'Year': 2017,
        'Month': 6,
        'Weekday': 5,
        'TextSize': 0})

    description = input['Description']
    input['TextSize'] = len(description)
    
    df = pd.DataFrame(input, index=[0])

    pipeline = load('finalmodel.sav')

    y_pred = pipeline.predict(df)

    st.session_state['answer99'] = y_pred[0]

    return y_pred[0]

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(txtDescription):   
    prediction=classifier.predict([txtDescription])
    print(prediction)
    return prediction

questions = ["**Which country you are from?**", "**Which Locality you are from?**", "**What is your gender?**","**What is your employment type?**","**Which Industrial sector?**",
            "**What is the potential accident level?**","**What is the Critical Risk?**","**Please describe the accident in detail**","**Based on the details you shared, it looks like the severity level is **"]

#questions = ["What is your name","What is your age",""]
size = len(questions)

if 'globalflag' not in st.session_state:
    st.session_state.globalflag = 0

if 'question' not in st.session_state:
    st.session_state.question = ''

if 'count' not in st.session_state:
    st.session_state.count = 0

counter = str(st.session_state.count)
previouscounter = str(st.session_state.count - 1)
if(st.session_state.count - 1 <= 0):
    previouscounter = str(0)    

html_temp = """
<div style="background-color:grey;padding:5px">
<h2 style="color:white;text-align:center;">Semi Ruled Chat Bot - Industrial accidents</h2>
</div>
"""
st.markdown(html_temp,unsafe_allow_html=True)

c1,c2 = st.beta_columns(2)

with c1:
    rollingtext = st.session_state.question
    placeholder = st.empty()

    answer = st.text_input("Type your answer", value="", key=counter)

    with placeholder.beta_container():

        if(st.session_state.count < size):
            #Appending the answer to the chat text
            rollingtext = rollingtext+"\n\n"+st.session_state[previouscounter]

            #Store the answers to the session state
            answerkey = 'answers' + previouscounter
            st.session_state[answerkey] = st.session_state[previouscounter]

            #To add the next question to the rolling text
            nextquestion = questions[st.session_state.count]

            #Updating the state session with the rolling text
            rollingtext = rollingtext+"\r\n\n"+nextquestion

            #Predict the model if the details are all captured?
            if(st.session_state.count == 8):
                answers = processinput()
                rollingtext = rollingtext + "\r\n" + "**" + str(answers) + "**"

            st.session_state.question = rollingtext
            st.markdown(rollingtext)

            #Incrementing the counter by 1
            st.session_state.count+=1

        else:
            st.markdown(rollingtext)


#if st.button("Reset and Start new Chat"):
#    for key in st.session_state.keys():
#        del st.session_state[key]

#    st.session_state.question = questions[0]
#    st.session_state.count = 0

with c2:

    placeholder2 = st.empty()
    
    with placeholder2.beta_container():

        for key in st.session_state.keys():
            if(key.startswith('answer')):
                st.write(st.session_state[key])
