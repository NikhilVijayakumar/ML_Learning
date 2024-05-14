# Example usage:
source_image = "C:/Users/nikhi/Pictures/Upscale/data sample/unique face/unique_1.png"
target_folder = "C:/Users/nikhi/Pictures/Upscale/data sample/unique face"
base_filename = "euro_face"



from usecase.face_match_usecase import process_and_report

def match():
    process_and_report(source_image, target_folder, base_filename)