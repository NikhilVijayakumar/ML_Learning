import requests
import json

url = "https://dcb7-3-135-152-169.ngrok-free.app/sdapi/v1/txt2img"

payload = json.dumps({
  "prompt": "Beautiful young 22 year old woman,cute face,pretty,attractive",
  "negative_prompt": "Unattractive features, asymmetrical face, dull complexion, unkempt appearance, and lack of makeup monochrome:1.3), (over saturated:1.3)((blurry)), duplicate, ((duplicate body parts)), (disfigured), (poorly drawn), (low res, boring, mutated, artefacts, bad art, gross, ugly, poor quality, low quality BadDream FastNegativeV2",
  "seed": -1,
  "sampler_name": "Euler",
  "batch_size": 1,
  "steps": 35,
  "cfg_scale": 7,
  "width": 512,
  "height": 512,
  "eta": 0,
  "sampler_index": "Euler"
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
