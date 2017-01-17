import base64
import json
import requests

def detect_text(path):

    with open(path, 'rb') as image_file:
        content = base64.b64encode(image_file.read())
        content = content.decode('utf-8')

    api_key = "YOUR_API_KEY"
    url = "https://vision.googleapis.com/v1/images:annotate?key=" + api_key
    headers = { 'Content-Type': 'application/json' }
    request_json = {
        'requests': [
            {
                'image': {
                    'content': content
                },
                'features': [
                    {
                        'type': "TEXT_DETECTION",
                        'maxResults': 10
                    }
                ]
            }
        ]
    }
    response = requests.post(
        url,
        json.dumps(request_json),
        headers
    )
    result = response.json()
    print(result['responses'][0]['textAnnotations'][0]['description'])

if __name__ == '__main__':
    detect_text("receipt.jpg")
