
import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("DecisionTree.pkl","rb")
regressor=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def Air_Quality_Index(PM2,PM10,NO,NO2,NH3,CO,SO2,O3,Benzene,Toluene,City,Air_Quality):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=regressor.predict([[PM2,PM10,NO,NO2,NH3,CO,SO2,O3,Benzene,Toluene,City,Air_Quality]])
    print(prediction)
    return prediction



def main():
    st.title("Air_Quality")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit BAir Quality ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    PM2 = st.text_input("PM2","Type Here")
    PM10 = st.text_input("PM10","Type Here")
    NO = st.text_input("NO","Type Here")
    NO2 = st.text_input("NO2","Type Here")
    NH3 = st.text_input("NH3","Type Here")
    CO = st.text_input("CO","Type Here")
    SO2 = st.text_input("SO2","Type Here")
    O3 = st.text_input("O3","Type Here")
    Benzene = st.text_input("BENZENE","Type Here")
    Toluene = st.text_input("TOLUENE","Type Here")
    City = st.text_input("City","Type Here")
    Air_Quality = st.text_input("Air_Quality","Type Here")
    O3 = st.text_input("O3","Type Here")
    result=""
    if st.button("Predict"):
        result=Air_Quality_Index(PM2,PM10,NO,NO2,NH3,CO,SO2,O3,Benzene,Toluene,City,Air_Quality)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    