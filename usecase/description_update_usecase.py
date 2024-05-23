import os
from utils.file_utils import read_file, write_file

def prepend_text_to_file(file_path, text):
    original_content = read_file(file_path)
    new_content = text + "\n" + original_content
    write_file(file_path, new_content)

def process_files_in_directory(directory, text_to_prepend):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            text_file_path = os.path.join(directory, filename)
            prepend_text_to_file(text_file_path, text_to_prepend)
            print(f"Prepended text to {text_file_path}")
