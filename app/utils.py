import os
import uuid
import shutil
from pathlib import Path


base_dir = Path(__file__).resolve().parent.parent
file_update_dir_name = "temporary_upload_data"
file_upload_dir = os.path.join(base_dir, file_update_dir_name)


def save_uploaded_file(uploaded_file, upload_dir=file_upload_dir):
    """
    Save a file uploaded via Streamlit's file_uploader to disk.
    Returns the path to the saved file.
    """
    # Create the upload directory if it doesn't exist
    os.makedirs(upload_dir, exist_ok=True)

    # Generate a unique filename to avoid conflicts
    unique_filename = f"{uuid.uuid4().hex}_{uploaded_file.name}"
    file_path = os.path.join(upload_dir, unique_filename)

    # Save file to disk
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return file_path


def delete_previous_uploaded_files():
    if os.path.exists(file_upload_dir):
        shutil.rmtree(file_upload_dir)
