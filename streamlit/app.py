import streamlit as st
import pandas as pd
import numpy as np

#title of the app
st.title('My first app')

#displat a simple text 
st.write('Here is our first attempt at using data to create a table:')

#creating a dataframe
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

#display the dataframe
st.write('This is a dataframe')
st.write(df)

#line chart
chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
)
st.line_chart(chart_data)
