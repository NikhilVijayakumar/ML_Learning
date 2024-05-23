import os
from utils.file_utils import copy_file


def find_and_copy_matching_files(source_dir, description_dir):
    for filename in os.listdir(source_dir):
        if filename.endswith(".png"):
            base_filename = os.path.splitext(filename)[0]
            txt_filename = base_filename + ".txt"
            txt_file_path = os.path.join(description_dir, txt_filename)

            if os.path.exists(txt_file_path):
                dest_txt_path = os.path.join(source_dir, txt_filename)
                copy_file(txt_file_path, dest_txt_path)
                print(f"Copied {txt_file_path} to {dest_txt_path}")