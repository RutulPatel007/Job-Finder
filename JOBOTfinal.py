from openai_api import chat_bot
import streamlit as st
import streamlit_chat
import openai
import textwrap

#Creating the chatbot interface
st.title("Jobot ")

# Storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []


def get_text():
    input_text = st.text_input("You: "," ", key="input")
    return input_text


user_input = get_text()

if user_input:
    output = chat_bot(user_input)
    # store the output
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:

    for i in range(len(st.session_state['generated']) - 1, -1, -1):
        streamlit_chat.message(st.session_state["generated"][i], key=str(i))
        streamlit_chat.message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')

