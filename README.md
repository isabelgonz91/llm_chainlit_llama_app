# LLM Chainlit Application

This is a sample application using Chainlit to generate answers to questions based on content from a text file with Llama3.

## Description

The application takes a user question, reads content from a text file, and generates a response using a language model hosted at a specific endpoint.

## Requirements

- Python 3.11
- Chainlit
- requests

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/llm_chainlit_app.git
    cd llm_chainlit_app
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

Make sure your `chainlit.yaml` file is correctly configured. Here is an example:

```yaml
entry_point: main.py
port: 8000
debug: true
