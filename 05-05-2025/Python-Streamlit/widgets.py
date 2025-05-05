import streamlit as st
import pandas as pd

st.title("Streamlite text input")

name = st.text_area("Enter Your name")

age = st.slider("select your age:", 0, 100, 25)
st.write(f"Your age: {age}")

options = ["Java", "React", "Javascript", "Python"]
choice = st.selectbox("Choose Your favourite language: ", options)
st.write(f"You selected {choice}")

st.write(f"Your age is {age}")
if name:
    st.write(f"Hello {name}")
    
    
data = {
    "Name" : ["John", "Mary", "peter", "Sam"],
    "Age" : [23, 25, 28, 30],
    "City": ["NewYork", "Chicago", "France", "Seattle"]
}

df = pd.DataFrame(data)
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file:", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)