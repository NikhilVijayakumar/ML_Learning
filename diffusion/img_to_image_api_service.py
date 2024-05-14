import requests
from diffusion.api_request_builder import ApiRequestBuilder


class ImgToImgApiService:
    def __init__(self):
        self.request_builder = ApiRequestBuilder()

    def img_to_img_api(self, data):
        url = self.request_builder.get_img_to_image_url()
        headers = self.request_builder.get_default_headers()

        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            print(f"img_to_img_api success")
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None
