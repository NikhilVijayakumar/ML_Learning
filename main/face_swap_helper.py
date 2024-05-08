from usecase.face_swap_usecase import swap_face_dir

source_image = "C:/Users/nikhi/Pictures/Upscale/character/Female/gen/Isabelle_Peter.png"
target_folder = "C:/Users/nikhi/Pictures/Upscale/Lora sample/Real1"
output_dir = "C:/Users/nikhi/Pictures/Upscale/character/Female/IsabellePeter"


def swap_images():
    swap_face_dir(source_image, target_folder, output_dir)
