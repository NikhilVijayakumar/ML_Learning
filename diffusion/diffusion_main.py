from png_info_api_service import PngInfoApiService
from utils.base64_utils import image_to_base64, base64_to_image

source_image = "C:/Users/nikhi/Pictures/Upscale/Tabitha Kaiser/Tabitha_Kaiser.png"

# Example usage
#image_path = "example_image.jpg"
#base64_data = image_to_base64(image_path)
#print("Base64 encoding of the image:", base64_data)

# Convert back to image
#save_path = "example_image_new.jpg"
#base64_to_image(base64_data, save_path)
#print("Image saved as:", save_path)


c





def main():
    api_service = PngInfoApiService()
    image_base64 = image_to_base64(source_image)
    parse_png_info(api_service.get_png_info(image_base64))


if __name__ == "__main__":
    main()
