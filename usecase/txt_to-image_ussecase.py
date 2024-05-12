import os
import uuid
from diffusion.txt_to_image_api_service import TxtToImgApiService
from prompt.beautiful_woman import generate_beautiful_woman_prompt
from utils.base64_utils import base64_to_image


def txt_to_image_usecases(save_dir):
    api_service = TxtToImgApiService()
    ethnicity = ["European", "Korean", "Latina"]
    selected_ethnicity = ethnicity[0]
    prompt = generate_beautiful_woman_prompt(selected_ethnicity)
    data = {
        "prompt": prompt,
        "negative_prompt": "Unattractive features, asymmetrical face, dull complexion, unkempt appearance, and lack "
                           "of makeup monochrome:1.3), (over saturated:1.3)((blurry)), duplicate, ((duplicate body "
                           "parts)), (disfigured), (poorly drawn), (low res, boring, mutated, artefacts, bad art, "
                           "gross, ugly, poor quality, low quality BadDream FastNegativeV2",
        "seed": -1,
        "sampler_name": "DPM++2M Kerras",
        "batch_size": 1,
        "steps": 35,
        "cfg_scale": 7,
        "width": 512,
        "height": 512,
        "eta": 0,
        "sampler_index": "DPM++2M Kerras",
        "send_images": True,
        "save_images": False
    }
    response_data = api_service.txt_to_img_api(data)
    images = response_data.get('images', [])
    for i, base64_string in enumerate(images, 1):
        unique_filename = str(uuid.uuid4())
        filename = f"{selected_ethnicity}_{unique_filename}_{i}.png"
        save_path = os.path.join(save_dir, filename)
        base64_to_image(base64_string, save_path)