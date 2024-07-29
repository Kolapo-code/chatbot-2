import streamlit as st
import requests
from elasticsearch import Elasticsearch
from transformers import pipeline

# Show title and description.
st.title("💬 Chatbot")
st.write(
    "This is a simple chatbot that uses Hugging Face's models to generate responses and Elasticsearch for document retrieval. "
    "To use this app, you need to provide an Elasticsearch server URL and Hugging Face API key, which you can get [here](https://huggingface.co/settings/tokens). "
)

# Ask user for their Elasticsearch server URL and Hugging Face API key via `st.text_input`.
es_url = st.text_input("Elasticsearch Server URL")
hf_api_key = st.text_input("Hugging Face API Key", type="password")

if not es_url or not hf_api_key:
    st.info("Please add your Elasticsearch server URL and Hugging Face API key to continue.", icon="🗝️")
else:
    # Create an Elasticsearch client.
    es = Elasticsearch([es_url])

    # Initialize the Hugging Face model
    generator = pipeline("text-generation", model="gpt2", use_auth_token=hf_api_key)

    # Create a session state variable to store the chat messages. This ensures that the messages persist across reruns.
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display the existing chat messages via `st.chat_message`.
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Create a chat input field to allow the user to enter a message. This will display automatically at the bottom of the page.
    if prompt := st.chat_input("What is up?"):

        # Store and display the current prompt.
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Perform document retrieval from Elasticsearch
        search_query = {
            "query": {
                "match": {
                    "content": prompt
                }
            }
        }
        search_results = es.search(index="documents", body=search_query)

        # Extract the retrieved document content
        retrieved_docs = [hit["_source"]["content"] for hit in search_results["hits"]["hits"]]

        # Generate a response using the Hugging Face model
        context = " ".join(retrieved_docs)
        input_text = f"{context}\nUser: {prompt}\nAssistant:"

        generated_response = generator(input_text, max_length=150, num_return_sequences=1)
        response = generated_response[0]["generated_text"].replace(input_text, "").strip()

        # Display the response
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})