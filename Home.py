import pandas as pd
import pydeck as pdk
import streamlit as st
from streamlit import title


def homepage():
    st.header("Welcome to my Portfolio!")
    st.write("Thank you for taking the time to visit my web app. I created this website with the intent of sharing projects that I have completed throughout my time at Bentley University. The goal of sharing this website is to give you a better idea of my in class experiences as well as to practice my coding skills. Please feel free to navigate through the pages which include a personal bio, my favorite programs I have written, and various finance related projects I have completed.")
    st.divider()
    st.write("If you would like to view the code I used to put together this web app, please feel free to click the button below to be taken to my github repository")
    st.write("https://github.com/seamus-stirling/portfolio")


def main ():
    homepage()

main()