import streamlit as st
import sys
import os

sys.path.append(os.path.abspath("src"))

from predict import predict_class
from actions import perform_action

st.title("🤖 Smart Personal Assistant Bot")

user_input = st.text_input("Enter your command")

if st.button("Execute"):

    if user_input.strip() == "":
        st.warning("Please enter a command")

    else:
        tag = predict_class(user_input)

        if tag == "unknown":
            st.error("I didn't understand that.")

        else:
            response = perform_action(tag)
            st.success(response)
