import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Set the page configuration
st.set_page_config(page_title="Mini Agent", 
page_icon=":robot:",
layout="wide",
initial_sidebar_state="expanded",
)


st.title("Mini Agent")
user_message = st.text_input("Message", placeholder="Type something…")
if user_message:
    st.write("You entered:", user_message)
