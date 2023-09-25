import streamlit as st
from datetime import datetime

# text input
st.write("1.Name")
name= st.text_input("Enter Your Name",max_chars=50,help="Enter Alphabeticals Only")

#Age
st.write("2.Age")
Age= st.number_input("Enter Your Age",help="Age should between 1 and 101",step=1,max_value=101,min_value=21)


#password
st.write("3.Password")
password=st.text_input("Enter Your Password",type='password',help="Password must be of more than 8 characters")

#Text Area
st.write("4.Text Description")
Description=st.text_area("Enter some descripton here",height=10,max_chars=500,help="Not more than 500 characters are allowed")

st.write("Hi,"+name)

#Date of Booking
st.write("5.Booking Date")
today= datetime.now().date()

date=st.date_input("Enter the booking Date",min_value=today,max_value=today.replace(year=today.year+1))
st.write("you have selected :",datetime.strftime(date,'%m/%d/%Y'))