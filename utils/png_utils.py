import os
from PIL import Image

def convert_images_to_png(directory):
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        # Check if the file is a JPEG or WebP image
        if filename.lower().endswith(('.jpg', '.jpeg', '.webp')):
            try:
                # Open the image
                with Image.open(filepath) as img:
                    # Convert the image to RGB mode if it's not already in that mode
                    if img.mode != "RGB":
                        img = img.convert("RGB")
                    # Create the new filename with PNG extension
                    new_filename = os.path.splitext(filename)[0] + ".png"
                    new_filepath = os.path.join(directory, new_filename)
                    # Save the image as PNG
                    img.save(new_filepath, "PNG")
                # Delete the original image file
                os.remove(filepath)
                print(f"Converted and deleted: {filename}")
            except Exception as e:
                print(f"An error occurred processing {filename}: {e}")


