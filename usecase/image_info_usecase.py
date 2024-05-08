import os
import json
from diffusion.png_info_api_service import PngInfoApiService
from utils.base64_utils import image_to_base64

def save_image_info(folder_path, output_dir):
    # Hardcoded supported extensions
    supported_extensions = {'.png', '.jpg', '.jpeg', '.webp'}

    # Check if the folder path exists
    if not os.path.isdir(folder_path):
        print("Error: Invalid folder path")
        return

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Initialize API service
    api_service = PngInfoApiService()

    # Initialize batch counter
    batch_counter = 1

    # Initialize index
    index = 1

    # Initialize batch JSON data
    batch_data = []

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

            # Create dictionary for current file
            file_info = {
                "filename": file_name,
                "prompt": prompt,
                "negative_prompt": negative_prompt,
                "steps": steps,
                "sampler": sampler,
                "CFG_scale": scale_CFG,
                "seed": seed,
                "width": width,
                "height": height,
                "denoising_strength": denoising_strength
            }

            # Append file info to batch data
            batch_data.append(file_info)

            # If batch size reaches 20 or end of files, save batch JSON file
            if len(batch_data) == 20 or index == len(os.listdir(folder_path)):
                # Create JSON object with data array
                json_object = {"data": batch_data}

                # Write JSON data to file
                output_json_path = os.path.join(output_dir, f"batch_{batch_counter}.json")
                with open(output_json_path, 'w') as json_file:
                    json.dump(json_object, json_file, indent=4)

                print(f"Processed files and stored details in '{output_json_path}'")

                # Reset batch data and increment batch counter
                batch_data = []
                batch_counter += 1

            # Increment index
            index += 1

# Example usage:
# folder_path = "path/to/your/folder"
# output_dir = "path/to/output/directory"
# process_files(folder_path, output_dir)
