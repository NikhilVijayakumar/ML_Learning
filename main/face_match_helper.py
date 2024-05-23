# Example usage:
source_image = "C:/Users/nikhi/Pictures/Upscale/character/Female/Completed/Shinta Elias.png"
target_folder = "C:/Users/nikhi/Pictures/Upscale/character/Female/Completed/Shinta Elias"
similarity_percentage = 55


from usecase.face_match_usecase import process_and_similarity

def match():
    process_and_similarity(source_image, target_folder,similarity_percentage)