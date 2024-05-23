from usecase.description_update_usecase import process_files_in_directory

directory = "C:/Users/nikhi/Pictures/Upscale/Lora sample/Asian"
text = "a beautiful Korean V-shaped face woman, with a small face, a slender jawline a sharp chin, black big rounded eyes, double eyelids, a small pointy nose with a high bridge, a round forehead, straight eyebrows, smallmouth, plump lips, Pale skin, Aegyo-sal makeup"


def update_description():
    process_files_in_directory(directory, text)
