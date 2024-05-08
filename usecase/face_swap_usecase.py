from utils.base64_utils import image_to_base64, base64_to_image
from diffusion.roop_api_service import RoopApiService  # Importing the RoopApiService class
import os


def swap_face(source_image_path, target_image_path, output_image_path):
    # Initialize RoopApiService
    roop_api_service = RoopApiService()

    # Convert source and target images to base64
    source_image = image_to_base64(source_image_path)
    target_image = image_to_base64(target_image_path)

    # Construct payload
    payload = {
        "source_image": source_image,
        "target_image": target_image,
        "face_index": [0],
        "scale": 1,
        "upscale_visibility": 1,
        "face_restorer": "None",
        "restorer_visibility": 1,
        "model": "E:\\AI\\stable-diffusion-webui\\models\\roop\\inswapper_128.onnx"
    }

    try:
        # Call API using RoopApiService
        response_data = roop_api_service.roop_image_api(payload)

        if response_data:
            # Extract image data from response
            image_base64 = response_data.get("image", "")

            # Convert base64 image to file
            base64_to_image(image_base64, output_image_path)

            print("Image saved as:", output_image_path)
        else:
            print("Error: No response data received")
    except Exception as e:
        print("Error:", e)


def swap_face_dir(source_image_path, target_directory, output_directory):
    # Check if the target and output directories exist, if not, create them
    if not os.path.isdir(target_directory):
        print("Error: Target directory does not exist")
        return
    if not os.path.isdir(output_directory):
        os.makedirs(output_directory)

    # Supported image extensions
    supported_extensions = {'.png', '.jpg', '.jpeg', '.webp'}

    # Loop through each file in the target directory
    for filename in os.listdir(target_directory):
        filepath = os.path.join(target_directory, filename)

        # Skip directories
        if os.path.isdir(filepath):
            continue

        # Check if the file is an image
        _, extension = os.path.splitext(filename)
        if extension.lower() not in supported_extensions:
            continue

        # Generate output file path
        output_filename = f"{os.path.basename(source_image_path).split('.')[0]}_{filename.split('.')[0]}{extension}"
        output_filepath = os.path.join(output_directory, output_filename)

        # Process the image
        swap_face(source_image_path, filepath, output_filepath)


