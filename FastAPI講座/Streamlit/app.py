import streamlit as st
import pandas as pd
import numpy as np

if st.button("click me"):
    st.write("clicked")

if st.checkbox("click me"):
    st.write("OKOKO")

options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.write(f'You selected:{options}')   

number = st.sidebar.slider("Pick a num", 0 , 100, 40, 5)
st.sidebar.write(f'Your selected number is {number}')

left_col, right_col = st.columns(2)
left_col.slider("Pick a age", 0, 50)
right_col.write("This is right")