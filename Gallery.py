import pandas as pd
import pydeck as pdk
import streamlit as st
from streamlit import title


def homepage():
    st.set_page_config(page_title="Seamus's Personal Portfolio", layout="wide")
    st.title("Seamus's Personal Portfolio")
    pages = st.navigation([
        st.Page("Home.py", title="Home"),
        st.Page("About_Me.py", title="About Me"),
        st.Page("finance_projects.py", title="Finance Projects"),
        st.Page("coding_projects.py", title="Coding Projects")
    ])
    pages.run()

def main():
    homepage()

main()