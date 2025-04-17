from usecase.face_swap_usecase import swap_face_dir

lora_asian = "C:/Users/nikhi/Pictures/Upscale/Lora sample/Asian"
lora_euro = "C:/Users/nikhi/Pictures/Upscale/Lora sample/Euro"
lora_latina = "C:/Users/nikhi/Pictures/Upscale/Lora sample/Latina"

folder = "C:/Users/nikhi/Pictures/Upscale/character/face/ot/Priya Rai/"

source_image = "C:/Users/nikhi/Pictures/Upscale/character/face/ot/Deekshita.png"
output_dir = "C:/Users/nikhi/Pictures/Upscale/character/face/ot/Deekshita/Completed/pr_su"


def swap_images():
    swap_face_dir(source_image, folder, output_dir)
