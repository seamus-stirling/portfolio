import pandas as pd
import pydeck as pdk
import streamlit as st

def bio_page ():
    st.set_page_config(layout="wide")
    st.header("Coding Projects")
    column_1, column_2 = st.column_config
    with column_1:
        st.write("this is column 1")
    with column_2:
        st.write("this is column 2")

def main ():
    bio_page()
    return

main()