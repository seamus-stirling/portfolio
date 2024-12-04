import pandas as pd
import pydeck as pdk
import streamlit as st

def homepage():
    st.set_page_config(layout="wide")
    st.header("Welcome to my Portfolio!")
    st.write("Thank you for taking the time to visit my web app. I created this website with the intent of sharing projects that I have completed throughout my time at Bentley University. The goal of sharing this website is to give you a better idea of my in class experiences as well as to practice my coding skills. Please feel free to navigate through the pages which include a personal bio, my favorite programs I have written, and various finance related projects I have completed.")
    return



def main ():
    homepage()
    return

main()