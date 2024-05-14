import os
import uuid
from diffusion.img_to_image_api_service import ImgToImgApiService
from prompt.beautiful_woman import generate_beautiful_woman_prompt
from utils.base64_utils import base64_to_image, image_to_base64


def img_to_image_usecase(source_image_path, selected_ethnicity, save_dir,formatted_prompt=None):
    api_service = ImgToImgApiService()
    source_image = image_to_base64(source_image_path)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    if formatted_prompt is None:
        formatted_prompt = f"{ generate_beautiful_woman_prompt(selected_ethnicity)}"

    data = {
        "prompt": formatted_prompt,
        "negative_prompt": "Unattractive features, asymmetrical face, dull complexion, unkempt appearance, and lack "
                           "of makeup monochrome:1.3), (over saturated:1.3)((blurry)), duplicate, ((duplicate body "
                           "parts)), (disfigured), (poorly drawn), (low res, boring, mutated, artefacts, bad art, "
                           "gross, ugly, poor quality, low quality BadDream FastNegativeV2",
        "seed": -1,
        "sampler_name": "DPM++ 2M Karras",
        "batch_size": 1,
        "steps": 35,
        "cfg_scale": 7,
        "width": 512,
        "height": 512,
        "denoising_strength": 0.75,
        "init_images": [
            source_image
        ],
        "eta": 0,
        "sampler_index": "DPM++ 2M Karras",
        "send_images": True,
        "save_images": False
    }
    # print(data)
    response_data = api_service.img_to_img_api(data)
    if response_data is not None:
        images = response_data.get('images', [])
        for i, base64_string in enumerate(images, 1):
            unique_filename = str(uuid.uuid4())
            filename = f"{selected_ethnicity}_{unique_filename}_{i}.png"
            save_path = os.path.join(save_dir, filename)
            base64_to_image(base64_string, save_path)
            print(f"image saved successfully {save_path}")
    else:
        print("api failed")

def folder_to_image_usecase(folder_path):
    # Hardcoded supported extensions
    supported_extensions = {'.png', '.jpg', '.jpeg', '.webp'}
    ethnicity = ["European", "Korean", "Latina"]
    selected_ethnicity = ethnicity[0]
    # Check if the folder path exists
    output_dir = os.path.join(folder_path, f"output_{selected_ethnicity}")
    if not os.path.isdir(folder_path):
        print("Error: Invalid folder path")
        return

    # Initialize index
    index = 1

    # Iterate over files in the folder
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, extension = os.path.splitext(file_name)

        # Check if the extension is supported

        if extension.lower() in supported_extensions:
            source_image = file_path
            img_to_image_usecase(source_image,selected_ethnicity , output_dir,f"Beautiful woman,cute face,pretty,attractive")