import streamlit as st
import pandas as pd
import pickle
st.write("""
# Loan status Prediction
 """)
svm_classifier = open('Loan_Model.pkl','rb')
classifier = pickle.load(svm_classifier)
b1=b2=b3=0
account_no = st.text_input('Account number')
fn = st.text_input('Full Name')
income = st.text_input("Enter the income(in hundreds)  ")
coincome = st.text_input("Enter the coincome(in hundreds)  ")
loanAmount = st.text_input("Enter the loan amount (in hundreds) ")
#gender =  st.text_input("Enter the Gender (M/F)  ")
gender=st.radio("Select gender",('Male','Female'))
if gender=='Male':
	gender=1
else:
	gender=0
credit=st.radio("do you have credit history",('yes','no'))
if credit=='yes':
	credit=1
else:
	credit=0
martial=st.radio("Select martial status",('yes','no'))
if martial=='yes':
	martial=1
else:
	martial=0
graduate=st.radio("Select graduate or not ",('yes','no'))
if graduate=='yes':
	graduate=1
else:
	graduate=0
selfemploy=st.radio("Select self employee or not ",('yes','no'))
if selfemploy=='yes':
	selfemploy=1
else:
	selfemploy=0
dependents = st.radio("choose the no of dependents ",("zero","one","two ","three","more than three"))
if dependents=="zero":
	dependents=0
elif dependents=="one":
	dependents=1
elif dependents=="two":
	dependents=2
elif dependents=="three":
    dependents=3
else:
	dependents=4
property = st.radio("choose the property type ",("rural","semi urban","urban "))
if property=="rural":
	property=0
elif property=="semi urban":
	property=1
else:
	property=2
submit = st.button("Predict")
if submit:
        result = classifier.predict([[gender, martial, dependents, graduate, selfemploy, income, coincome,loanAmount, credit, property]])
        if result == 0:
                st.error("Hello: " + fn +" || ""Account number: "+account_no +' || ''According to our Calculations, you will not get the loan from Bank')

               # st.markdown("I am very sorry... ***It seems you will have no loan*** :cry:")
        else :
                st.success("Hello: " + fn +" || ""Account number: "+account_no +' || ''Congratulations!! you will get the loan from Bank')
                #st.markdown("congrats")
