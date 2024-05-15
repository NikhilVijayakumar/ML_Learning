from utils.file_utils import rename_files

# Specify the folder path and base name
folder_path = "C:/Users/nikhi/Pictures/Upscale/Lora sample/Euro"
base_name = "ref_lora_euro"

def rename():
    rename_files(folder_path, base_name)

