import streamlit as st
from langchain.llms import OpenAI

st.title('🦜🔗 Quickstart App')
st.write("This is my first Streamlit application.")
st.success("The app is running correctly.")

openai_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))

with st.form('my_form'):
    text = st.text_area(
        'Enter text:',
        'What are the three key pieces of advice for learning how to code?'
    )
    submitted = st.form_submit_button('Submit')

    if not openai_api_key.startswith('sk-'):
        st.warning('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', icon='⚠️')

    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)
