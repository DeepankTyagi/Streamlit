import streamlit as st

def rate_yourself():
	with st.sidebar:
		st.title("Rate Yoursef")
		languages= st.text_input("Enter the languages here in a comma separated manner:",value="Python")
		languages=[language.strip() for language in languages.split(',')]
	st.subheader("How would Rate Yourself in the following:")
	for language in languages:
		# st.write(language)
		st.slider(language,max_value= 10.0,min_value=0.0,step=0.5)

def bmicalc():
	st.title("BMI Calulator")
	with st.form("BMI Calulator",clear_on_submit=False):
		col1,col2,col3=st.columns([3,2,1])
	with col1:
		weight=st.number_input("Enter your weight in Kg", help= "Number must be greater than 0")
	with col2:
		height=st.number_input("Enter your height in meters", help= "Number must be greater than 0")
	with col3:
		submit=st.form_submit_button("Calculate")

	if submit:
		BMI=round(weight/(height**2),2)
		if BMI<=18.5:
			st.error("Underweight")
		elif BMI >18.5 and BMI <= 24.9:
			st.success("Healthy/Normal weight")
		elif BMI>25.0 and BMI <= 29.9:
			st.warning("Overweight")
		elif BMI>=30:
			st.error("Obese")


choice= st.sidebar.selectbox("Menu",options={"BMI Calulator","Rate Yourself"})
if choice== "BMI Calulator":
	bmicalc()
elif choice=="Rate Yourself":
	rate_yourself()