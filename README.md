# Streamlit Chatbot with Elasticsearch and Hugging Face

This is a simple chatbot application built using Streamlit. The application uses Elasticsearch for document retrieval and Hugging Face's transformers for generating responses. 

## Features

- **Multimodal RAG**: Combines document retrieval and response generation.
- **Elasticsearch**: Retrieves relevant documents based on user queries.
- **Hugging Face**: Generates responses using the GPT-2 model or other Hugging Face models.
- **Streamlit Interface**: Provides a simple and interactive web interface.

## Prerequisites

- Python 3.7 or higher
- Elasticsearch server (local or hosted)
- Hugging Face API key

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/streamlit-chatbot.git
    cd streamlit-chatbot
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure your Elasticsearch server is running and has an index named `documents`.

## Usage

1. ### How to run it on your own machine

Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

Run the app

   ```
   $ streamlit run streamlit_app.py
   ```

2. Open your browser and go to `http://localhost:8501`.

3. Enter your Elasticsearch server URL and Hugging Face API key when prompted.

## Elasticsearch Setup

1. Install Elasticsearch (if not already installed):
    - For local installation, download from [Elastic's website](https://www.elastic.co/downloads/elasticsearch) and follow the instructions.
    - For a hosted service, consider using [Elasticsearch Service](https://www.elastic.co/elasticsearch/service).

2. Start your Elasticsearch server:
    ```bash
    ./bin/elasticsearch
    ```

3. Create an index and add documents:
    ```bash
    # Create an index named 'documents'
    curl -X PUT "localhost:9200/documents"

    # Add a document to the index
    curl -X POST "localhost:9200/documents/_doc/1" -H 'Content-Type: application/json' -d'
    {
      "content": "This is the content of the document."
    }
    '
    ```

## Example Document
Ensure your documents in Elasticsearch have the following structure:
```json
{
  "content": "This is the content of the document."
}
