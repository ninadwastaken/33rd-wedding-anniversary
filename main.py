import streamlit as st
import os
st.set_page_config(layout='wide')


st.markdown("<h1 style='text-align: center; color: white;'>HAPPY 33RD ANNIVERSARY!!!!</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: white;'>thank you both for existing <3<3</h1>", unsafe_allow_html=True)
st.info("hope there's many many more")
st.info(r"also thank you for having us")
st.info("have a wonderful day")
st.info("we made a small collage hehehe")

print(os.listdir("images"))
files = os.listdir("images")

col1, col2 = st.columns(2)

with col1:
    for file in files[::2]:
        st.image(f"images/{file}")
with col2:
    for file in files[1::2]:
        st.image(f"images/{file}")

st.markdown("<h1 style='text-align: center; color: white;'>june 20: truly a good day</h1>", unsafe_allow_html=True)




