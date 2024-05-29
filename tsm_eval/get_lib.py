import os
import requests
from dotenv import load_dotenv

load_dotenv()

# use to inspect uploaded files via SDK

api_key = os.environ["AI21_API_KEY"]

url = "https://api.ai21.com/studio/v1/library/files"
headers = {"Authorization": f"Bearer {api_key}"}

files = {"file": open("data/interview_transcript.txt", "rb")}

response = requests.get(url=url, headers=headers)
print(response.content)