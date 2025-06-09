import streamlit as st
from pathlib import Path
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain.indexes import VectorstoreIndexCreator

from utils import save_uploaded_file, delete_previous_uploaded_files

# Load environment variables
load_dotenv(override=True)
base_dir = Path(__file__).resolve().parent.parent

# Initialize session state
if "upload_key" not in st.session_state:
    st.session_state.upload_key = "initial"

delete_previous_uploaded_files()

st.title("Upload PDF(max 100 page & 10MB)")
uploaded_file = st.file_uploader(
    "Choose a PDF file", type="pdf", key=st.session_state.upload_key
)

pdf_loader = None
pages = None
is_file_valid = False


def get_file_size(uploaded_file):
    if uploaded_file is None:
        return None

    return uploaded_file.size / (1024 * 1024)  # Convert to MB


if uploaded_file is not None:
    file_path = save_uploaded_file(uploaded_file)
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! Ask me about your document?"}
    ]
    st.write("File uploaded successfully!")

    with st.spinner("Wait for it...", show_time=True):
        file_size = get_file_size(uploaded_file)

        if file_size > 10:
            st.warning("File cannot be more than 10MB")
        else:
            pdf_loader = PyPDFLoader(file_path)
            pages = pdf_loader.load()

            if len(pages) > 100:
                st.warning("PDF with more than 100 pages are not supported")

        if pdf_loader and pages and len(pages) <= 100:
            is_file_valid = True
        else:
            st.session_state.upload_key = str(hash(st.session_state.upload_key))


if is_file_valid:
    st.write(f"Number of pages in the document: {len(pages)}")

    llm_model = "gpt-3.5-turbo"
    llm = ChatOpenAI(temperature=0.9, model=llm_model)

    index = VectorstoreIndexCreator(
        vectorstore_cls=DocArrayInMemorySearch,
        embedding=OpenAIEmbeddings(),
    ).from_loaders([pdf_loader])

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi! Ask me about your document?"}
        ]

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Chat input box
    prompt = st.chat_input("Say something...")

    if prompt:
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get assistant response from OpenAI
        with st.chat_message("assistant"):
            response = index.query(prompt, llm=llm)
            assistant_reply = response
            st.markdown(assistant_reply)

        # Save assistant reply to history
        st.session_state.messages.append(
            {"role": "assistant", "content": assistant_reply}
        )
