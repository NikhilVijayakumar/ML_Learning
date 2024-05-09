import os
from diffusion.png_info_api_service import PngInfoApiService
from utils.base64_utils import image_to_base64

def calculate_aspect_ratio(width, height):
    try:
        width = float(width)
        height = float(height)
        return width / height
    except (ValueError, TypeError):
        return None

def organize_images(folder_path):
    # Hardcoded supported extensions
    supported_extensions = {'.png', '.jpg', '.jpeg', '.webp'}

    # Check if the folder path exists
    if not os.path.isdir(folder_path):
        print("Error: Invalid folder path")
        return

    # Create directories if they don't exist
    error_dir = os.path.join(folder_path, "error")
    square_dir = os.path.join(folder_path, "square")
    non_square_dir = os.path.join(folder_path, "non_square")
    os.makedirs(error_dir, exist_ok=True)
    os.makedirs(square_dir, exist_ok=True)
    os.makedirs(non_square_dir, exist_ok=True)

    # Initialize API service
    api_service = PngInfoApiService()

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
            # Call API and parse PNG info
            image_base64 = image_to_base64(file_path)
            png_info = api_service.get_png_info(image_base64)

            # Extract required parameters
            parameters = png_info.get('parameters', {})
            prompt = parameters.get('Prompt', '')
            negative_prompt = parameters.get('Negative prompt', '')
            steps = parameters.get('Steps', '')
            sampler = parameters.get('Sampler', '')
            scale_CFG = parameters.get('CFG scale', '')
            seed = parameters.get('Seed', '')
            width = parameters.get('Size-1', '')
            height = parameters.get('Size-2', '')
            denoising_strength = parameters.get('Denoising strength', '')

            # Check for missing parameters
            missing_params = []

            # Check for missing parameters
            if not prompt:
                missing_params.append('Prompt')
            if not negative_prompt:
                missing_params.append('Negative prompt')
            if not width:
                missing_params.append('Width')
            if not height:
                missing_params.append('Height')


            if missing_params:
                print(f"Error: Missing parameters for '{file_name}': {', '.join(missing_params)}")
                os.replace(file_path, os.path.join(error_dir, file_name))
                continue

            # Calculate aspect ratio
            aspect_ratio = calculate_aspect_ratio(width, height)

            # Move to appropriate directory based on aspect ratio
            if aspect_ratio == 1:
                os.replace(file_path, os.path.join(square_dir, file_name))
                print(f"'{file_name}' is a square image. Moved to square directory.")
            else:
                os.replace(file_path, os.path.join(non_square_dir, file_name))
                print(f"'{file_name}' is a non-square image. Moved to non-square directory.")
