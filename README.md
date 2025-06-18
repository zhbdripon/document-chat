# Document QA Web App

This project is a Document Question Answering (QA) web application. Users can upload their PDF documents and interactively ask questions about the content. The app leverages modern LLM and vector database technology to provide accurate answers based on the uploaded document.

## Features
- Upload PDF documents (max 100 pages, 10MB)
- Ask questions about the uploaded document
- Get answers based on the document content
- Streamlit-based interactive web interface

## Requirements
- Python 3.9
- [pipenv](https://pipenv.pypa.io/en/latest/)

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd document-chat
   ```

2. **Create pipenv environment and install dependencies**
   ```bash
   pipenv install --dev
   pipenv shell
   ```

3. **Set up pre-commit hooks**
   ```bash
   pre-commit install
   ```

4. **Run linter manually (optional)**
   ```bash
   pre-commit run --all-files
   ```

5. **Run the Streamlit server**
   ```bash
   streamlit run app/main.py
   ```

## Usage
- Open your browser to the Streamlit URL (usually http://localhost:8501)
- Upload a PDF document
- Ask questions in the chat interface

## License
MIT
