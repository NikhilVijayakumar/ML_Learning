import requests
import json
from utils.base64_utils import image_to_base64,base64_to_image

source_image_path = "C:/Users/nikhi/Pictures/Upscale/Tabitha Kaiser/Tabitha_Kaiser.png"
target_image_path = "C:/Users/nikhi/Pictures/Upscale/Lora sample/Real1/LoraRef_37.png"
url = 'http://127.0.0.1:7860/roop/image'

# Payload data
source_image = image_to_base64(source_image_path)
target_image = image_to_base64(target_image_path)
payload = {
    "source_image":source_image,
    "target_image": target_image,
    "face_index": [0],
    "scale": 1,
    "upscale_visibility": 1,
    "face_restorer": "E:\\AI\\stable-diffusion-webui\\models\\Codeformer",
    "restorer_visibility": 1,
    "model": "E:\\AI\\stable-diffusion-webui\\models\\roop\\inswapper_128.onnx"
}

# Headers
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

# Convert payload to JSON string
payload_json = json.dumps(payload)

# Send POST request
response = requests.post(url, headers=headers, data=payload_json)

# Check response status code
if response.status_code == 200:
    # Parse response JSON
    response_data = response.json()

    # Extract image data from response
    image_base64 = response_data.get("image", "")
    output_dir = "C:/Users/nikhi/Pictures/Upscale/Tabitha Kaiser/ref1/"
    output_img = "tb_LoraRef_37.png"
    output = output_dir+output_img
    base64_to_image(image_base64,output)


    print(f"Image saved as {output}")
else:
    print("Error:", response.status_code)
