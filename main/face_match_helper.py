# Example usage:
source_image = "C:/Users/nikhi/Pictures/Upscale/Tabitha Kaiser/Tabitha_Kaiser.png"
target_folder = "C:/Users/nikhi/Pictures/Upscale/Tabitha Kaiser"
base_filename = "Tabitha_Kaiser"



from usecase.face_match_usecase import process_and_report

def match():
    process_and_report(source_image, target_folder, base_filename)