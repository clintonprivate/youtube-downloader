import requests

# Replace with your actual API key
api_key = "AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8"
video_id = "A67RYFTImTQ"

url = f"https://youtubei.googleapis.com/youtubei/v1/player?key={api_key}"

# Constructing the payload as required by the API
payload = {
    "context": {
        "client": {
            "clientName": "WEB",
            "clientVersion": "2.20230728.00.00"
        },
        "playbackContext": {
            "contentPlaybackContext": {
                "signatureTimestamp": "19369"
            }
        }
    },
    "videoId": video_id
}

headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    video_data = response.json()
    print(video_data)
else:
    print(f"Error: {response.status_code}")
    print(response.text)
