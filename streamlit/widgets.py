#https://streamlit.io/components

import streamlit as st
import pandas as pd
import numpy as np

#title
st.title('My first app')

#input text
name = st.text_input('Enter your name')     #text_input is a widget and used to enter text

#slider
age = st.slider('Enter your age', 1, 100 ,2 , help = 'age help function' )   #slider is a widget and used to select a range of values

#Selectbox

options = ['python', 'java', 'c++', 'ruby', 'javascript']
fav_lang = st.selectbox('What is your favorite programming language', options)   #selectbox is a widget and used to select a single value from a list

if name :
    st.write(f'''Hello {name.capitalize()} welcome to the app , 
                                            and your age is {age} and 
                                            your favorite language is {fav_lang}''')
    
    
#radio button
status = st.radio('What is your status', ('Active', 'Inactive'))   #radio is a widget and used to select a single value from a list
    
#multiselect
multiselect = st.multiselect('Select your favorite colors', ['red', 'green', 'blue', 'yellow'])   #multiselect is a widget and used to select multiple values from a list

#button
if st.button('Submit'):
    st.write('Button is clicked')
    
#dataframe
df = pd.DataFrame({
    'first_column': [1,2,3,4,5],
    'second_column': [10,20,30,40,50]})
st.write('This is a dataframe')
st.write(df)

#line chart
chart_dt = pd.DataFrame(
    np.random.randn(20,3),
    columns = ['a', 'b', 'c'])  #line chart is a widget and used to display line chart
st.line_chart(chart_dt)

#area chart
st.area_chart(chart_dt)   #area chart is a widget and used to display area chart

#barchart
st.bar_chart(chart_dt)   #bar chart is a widget and used to display bar chart


#FILE UPLOAD
upload_file = st.file_uploader('Choose a file to upload', type = 'csv')   #file_uploader is a widget and used to upload a file

#checkbox
if st.checkbox('I agree'):
    st.write('Great!')