from usecase.face_swap_usecase import swap_face_dir

lora_asian = "C:/Users/nikhi/Pictures/Upscale/Lora sample/Asian"
lora_euro = "C:/Users/nikhi/Pictures/Upscale/Lora sample/Euro"
lora_latina = "C:/Users/nikhi/Pictures/Upscale/Lora sample/Latina"

source_image = "C:/Users/nikhi/Pictures/Upscale/character/Female/Completed/Li Heimdal.png"
output_dir = "C:/Users/nikhi/Pictures/Upscale/character/Female/Completed/Li Heimdal"


def swap_images():
    swap_face_dir(source_image, lora_asian, output_dir)


