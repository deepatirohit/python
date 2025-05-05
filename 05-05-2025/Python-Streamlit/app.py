import streamlit as st
import pandas as pd
import numpy as np

# Streamlit is an open-source Python library that makes it easy to create and share custom web apps for 
# machine learning and data science

# title of the application
st.title("Hello Streamlit")

# display simple text
st.write("This is a simple text.")

# create a simple data frame
df = pd.DataFrame({
    'first column' : [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

# display the dataframe
st.write("Here displaying the dataframe")
st.write(df)

# create lie_chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),columns=['a', 'b', 'c']
)

st.line_chart(chart_data)