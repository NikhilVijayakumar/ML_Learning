from usecase.txt_to_image_usecase import txt_to_image_usecase
output_dir = "C:/Users/nikhi/Pictures/Upscale/character/face"
ethnicity = ["European", "Korean", "Latina"]
no_of_images = 4

def txt_to_image():
    for i in range(no_of_images):
        txt_to_image_usecase(ethnicity[0], output_dir)