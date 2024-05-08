import requests
from diffusion.api_request_builder import ApiRequestBuilder


class PngInfoApiService:
    def __init__(self):
        self.request_builder = ApiRequestBuilder()

    def get_png_info(self, image_base64):
        url = f"{self.request_builder.get_base_url()}/png-info"
        headers = self.request_builder.get_default_headers()
        data = {'image': image_base64}
        print(url)
        print(headers)
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None

