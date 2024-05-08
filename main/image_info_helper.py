# Example usage:
folder_path = "C:/Users/nikhi/Pictures/Upscale/Lora sample/Real1"
output_dir = "C:/Users/nikhi/Pictures/Upscale/Lora sample/Real1/json"
# process_files(folder_path, output_dir)



from usecase.image_info_usecase import save_image_info

def load_image_info():
    save_image_info(folder_path, output_dir)