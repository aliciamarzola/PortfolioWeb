import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")
    
with col2:
    st.title("Alicia Marzola")
    content = """Hello! My name is Alicia and I study Information Systems
    at the Federal University of Minas Gerais. I'm passionate about the field
    of data science and artificial intelligence, and I love to
    venture into projects with Python."""
    st.write(content)
    
below = """"Below you can find some apps I have
built in Python. Feel free to contact me!"""
st.write(below)

col3, col4 = st.columns(2)

df = pd.read_csv("venv/data.csv", sep=";")

with col3:
    for index, row in df.iterrows():
        if(index%2==0):
            st.header(row["title"])
            st.write(row["description"])
            st.image("images/"+row["image"])
            #st.write(f"[Source Code]({row['url]})")

    
with col4:
    for index, row in df.iterrows():
        if(index%2==1):
            st.header(row["title"])
            st.write(row["description"])
            st.image("images/"+row["image"])