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

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "VECTORSTORE_ID" not in st.session_state:
    st.session_state.VECTORSTORE_ID = None

# Function to load the vectorstore
def load_vectorstore():
    '''Load the vectorstore from the from .env file, then fallback to streamlit secrets'''
    try:
        vectorstore_id = os.getenv("VECTORSTORE_ID")

        if not vectorstore_id:
            try:
                vectorstore_id = st.secrets["VECTORSTORE_ID"]
            except Exception:
                pass
        if not vectorstore_id:
            st.error("No vectorstore ID found. Please set the VECTORSTORE_ID environment variable or add it to streamlit secrets.")
            return None

        return vectorstore_id
    except Exception as e:
        st.error(f"Error loading vectorstore: {e}")
        return None

#Define the initial message
INITIAL_MESSAGE = "Hi! I am a helpful mini agent. How can I help you today?"

# Build function reset_conversation
def reset_conversation():
    '''Reset the conversation history'''
    st.session_state.messages = [{
        "role": "assitant",
        "content": INITIAL_MESSAGE.strip()
    }]
    st.rerun()
    st.session_state.VECTORSTORE_ID = None
    st.success("Conversation reset successfully")

# Build function main
def main():
    '''Main function to run the app'''
    # Sidebar with reset button
    with st.sidebar:
        st.header("Settings")
        if st.button("Reset Conversation"):
            reset_conversation()

if __name__ == "__main__":
    main()