from usecase.add_description_usecase import find_and_copy_matching_files

description_dir = "C:/Users/nikhi/Pictures/Upscale/Lora sample/Latina"
source_dir= "C:/Users/nikhi/Pictures/Upscale/character/female/completed/Jolie Spencer"

def add_description():
    find_and_copy_matching_files(source_dir, description_dir)
