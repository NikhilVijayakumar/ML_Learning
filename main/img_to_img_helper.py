from usecase.ImgToImgUsecase import img_to_image_usecase,folder_to_image_usecase
output_dir = "C:/Users/nikhi/Pictures/Upscale/character/face"
ethnicity = ["European", "Korean", "Latina"]
no_of_images = 4
source_image = "C:/Users/nikhi/Pictures/Upscale/character/face/Latina/latina_1.png"
folder_path = "C:/Users/nikhi/Pictures/Upscale/data sample/unique face"

def img_to_image():
    for i in range(no_of_images):
        img_to_image_usecase(source_image,ethnicity[0], output_dir)

def folder_to_image():
    folder_to_image_usecase(folder_path)