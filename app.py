#Streamlit for the best for the front end UI 
#it also best for the we application

import streamlit as st
import pandas as pd
import numpy as np

# Title and subheader
st.title("Welcome to my Streamlit app")
st.subheader("A simple interactive application")

# Sidebar
st.sidebar.header("Input section")
user_name = st.sidebar.text_input("Enter your name", "Guest")

# Main body
st.write(f"Hello, {user_name}!")

# Example of number input
number = st.number_input("Pick a number", min_value=0, max_value=100, value=25)
st.write(f"You picked: {number}")

# DataFrame example
data = pd.DataFrame(np.random.randn(10, 5), columns=[f"column{i}" for i in range(1, 6)])
st.write("Random DataFrame:")
st.write(data)

# Chart example
st.header("Line Chart")
st.line_chart(data)

# File upload
st.header("File Upload")
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])  # Missing file uploader widget

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Uploaded DataFrame:")
    st.dataframe(df)

# Button
if st.button("Say Hello"):
    st.write("Hello Streamlit user!")

# Footer
st.write("______")
st.write("Built with ❤️ using Streamlit")
