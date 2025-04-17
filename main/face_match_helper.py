# Example usage:
source_image = "E:/AI/stable-diffusion-webui/outputs/txt2img-images/2024-05-31/00008-4265183855.png"
target_folder = "E:/AI/stable-diffusion-webui/outputs/txt2img-images/2024-05-31"
similarity_percentage = 55


from usecase.face_match_usecase import process_and_similarity

def match():
    process_and_similarity(source_image, target_folder,similarity_percentage)