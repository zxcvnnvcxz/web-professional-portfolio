import streamlit as st

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Edward Kang")
    content = """Hi, I am Edward! I work as a dynamic IT Support Technician with experience in event translation, 
    eager to return to work, hunting for my dream job in the tech industry. 
    Seeking my first full-time role in Data Analytics / Software
    Engineer with a major in Data Analytics"""
    st.info(content)