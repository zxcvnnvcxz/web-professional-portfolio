import streamlit as st
import pandas
import os

st.set_page_config(layout='wide')
image_path = os.path.join(os.getcwd(), "images/photo.png")
left_col, cent_col, last_col = st.columns(3)
with cent_col:
    st.image(image_path)

with st.container():
    # Use HTML to center both the image and the text
    st.markdown(
        """
        <div style="text-align: center;">
            <h1>Edward Kang</h1>
            <p>
                Hi, I am ! I've worked as a dynamic IT Support Technician with experience in event translation, 
                eager to return to work after a year of exchange abroad in Japan.
                Below are some of the apps I have built in Python.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

intro = ""
st.write(intro)
col3, empty_col, col4 = st.columns([1.5, 0.3, 1.5]) # Gap between the columns

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")