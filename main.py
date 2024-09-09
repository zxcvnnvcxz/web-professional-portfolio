import streamlit as st
import pandas

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Edward Kang")
    content = """Hi, I am Edward! I've worked as a dynamic IT Support Technician with experience in event translation, 
    eager to return to work after a year of exchange abroad in Japan."""
    st.info(content)

intro = """Below are some of the apps I have built in Python."""
st.write(intro)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])