import requests
from diffusion.api_request_builder import ApiRequestBuilder


class RoopApiService:
    def __init__(self):
        self.request_builder = ApiRequestBuilder()

    def roop_image_api(self, payload):
        headers = self.request_builder.get_default_headers()

        try:
            response = requests.post(self.request_builder.get_roop_image_url(), headers=headers, json=payload)
            response.raise_for_status()  # Raise exception for non-200 status codes
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None


