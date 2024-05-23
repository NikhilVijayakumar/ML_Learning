from usecase.description_update_usecase import process_files_in_directory

directory = "C:/Users/nikhi/Pictures/Upscale/character/female/completed/Jolie Spencer"
text = "Jolie Spencer"


def update_description():
    process_files_in_directory(directory, text)
