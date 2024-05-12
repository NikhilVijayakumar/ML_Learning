# Example usage:
source_image = "C:/Users/nikhi/Pictures/Upscale/character/face/Euro/euro_1.png"
target_folder = "C:/Users/nikhi/Pictures/Upscale/character/face/Euro"
base_filename = "euro_face"



from usecase.face_match_usecase import process_and_report

def match():
    process_and_report(source_image, target_folder, base_filename)