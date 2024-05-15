# Example usage:
source_image = "C:/Users/nikhi/Pictures/Upscale/character/Female/Completed/Ella Miller.png"
target_folder = "C:/Users/nikhi/Pictures/Upscale/character/Female/Completed/Ella Miller"
base_filename = "Abigail Read-"
similarity_percentage = 55


from usecase.face_match_usecase import process_and_similarity

def match():
    process_and_similarity(source_image, target_folder, base_filename,similarity_percentage)